import os
import requests
import logging

from botocore.client import Config

from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render
from django.views import generic
from django.conf import settings
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import Collection, Picture, Document
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .filters import DocumentFilter, ExamFilter
from .forms import PictureUploadForm, ExamUploadForm, ExamArchiveUploadForm
from .models import Collection, Document, Picture
from .tables import DocumentTable
from django.contrib.auth.decorators import permission_required


import os

logger = logging.getLogger('date')

def year_index(request):
    
    years = Collection.objects.dates('pub_date', 'year').reverse()
    year_albumcount = {}
    for year in years:
        year_albumcount[str(year.year)] = Collection.objects.filter(pub_date__year = year.year, type='Pictures').count()

    context = {
        'type': "pictures",
        'year_albums': year_albumcount
    }
    return render(request, 'archive/index.html', context)

def picture_index(request, year):
    collections = Collection.objects.filter(type="Pictures", pub_date__year=year).order_by('-pub_date')
    context = {
        'type': "pictures",
        'year' : year,
        'collections': collections,
    }
    return render(request, 'archive/picture_index.html', context)


def exams_index(request):
    collections = Collection.objects.filter(type="Exams").order_by('title')
    context = {
        'type': "exams",
        'collections': collections,
    }
    return render(request, 'archive/exams_index.html', context)



def exam_upload(request, pk):
    collection = Collection.objects.filter(pk=pk).first()
    if request.method == 'POST' and collection:
        form = ExamUploadForm(request.POST)
        if form.is_valid():
            if request.FILES.getlist('exams') is None:
                return redirect('archive:exams')
            for file in request.FILES.getlist('exams'):
                Document(document=file, title=form.cleaned_data['title'], collection=collection).save()
            logger.debug(f'User: {request.user} added files to {collection.title}')
        return redirect('archive:exams_detail', collection.pk)

    form = ExamUploadForm
    context = {
        'collection': collection,
        'exam_form': form,
    }
    return render(request, 'archive/exam_upload.html', context)



def exam_archive_upload(request):
    if request.method == 'POST':
        form = ExamArchiveUploadForm(request.POST)
        if form.is_valid():
            Collection(title=form.cleaned_data['title'], type='Exams').save()
            logger.debug(f'User: {request.user} added exams-archive: {form.cleaned_data["title"]}')
        return redirect('archive:exams')

    form = ExamArchiveUploadForm
    context = {
        'exam_form': form,
    }
    return render(request, 'archive/exam_upload.html', context)


class FilteredDocumentsListView(SingleTableMixin, FilterView):
    model = Document
    paginate_by = 15
    table_class = DocumentTable
    template_name = 'archive/document_index.html'
    filterset_class = DocumentFilter

    def get_table_data(self):
        filter_collection = self.request.GET.get('collection', '')
        filter_title_contains = self.request.GET.get('title__contains', '')
        
        if filter_collection or filter_title_contains:
            if filter_collection:
                return Document.objects.filter(
                    collection__type='Documents',
                    collection=filter_collection,
                    title__contains=filter_title_contains
                )
            else:
                return Document.objects.filter(
                    collection__type='Documents',
                    title__contains=filter_title_contains
                )
        else:
            return Document.objects.filter(collection__type='Documents')


class FilteredExamsListView(SingleTableMixin, FilterView):
    model = Document
    paginate_by = 15
    table_class = DocumentTable
    template_name = 'archive/exam_detail.html'
    filterset_class = ExamFilter

    def get_table_data(self):
        collection_pk = self.kwargs.get('pk')
        if collection_pk:
            Collection.objects.filter(pk=collection_pk)
            return Document.objects.filter(collection=collection_pk)
        else:
            return Document.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        context = super(FilteredExamsListView, self).get_context_data(*args, **kwargs)
        collection_pk = self.kwargs.get('pk')
        collection = Collection.objects.filter(pk=collection_pk).first()
        context['collection'] = collection
        return context


def picture_detail(request, year, album):
    collection = Collection.objects.filter(type="Pictures", pub_date__year=year, title=album).order_by('-pub_date')
    pictures = Picture.objects.filter(collection=collection[0])

    page = request.GET.get('page', 1)

    paginator = Paginator(pictures, 15)
    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        pictures = paginator.page(1)
    except EmptyPage:
        pictures = paginator.page(paginator.num_pages)

    context = {
        'type': "pictures",
        'year' : year,
        'album' : album,
        'collection' : collection[0],
        'pictures': pictures,
    }

    return render(request, 'archive/detail.html', context )

@permission_required('archive.add_collection')
def upload(request):
    if request.method == 'POST':
        form = PictureUploadForm(request.POST)
        if form.is_valid():
            if request.FILES.getlist('images') is None:
                return redirect('archive:pictures')
            collection = Collection(title=form['album'].value(), type='Pictures')
            collection.save()
            for file in request.FILES.getlist('images'):
                Picture(image=file, collection=collection).save()
        return redirect('archive:years')

    form = PictureUploadForm
    context = {
        'picture_form': form,
    }
    return render(request, 'archive/upload.html', context)


def clean_media(request):
    folders = os.walk(settings.MEDIA_ROOT)
    for f in folders:
        print(f[0])
        print(f[2])
        # If picture not in any collection, remove it.
    return redirect('archive:pictures')
import logging

from dateutil.relativedelta import relativedelta
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _

from members.models import (SUB_RE_SCALE_DAY, SUB_RE_SCALE_MONTH,
                            SUB_RE_SCALE_YEAR, Member, SubscriptionPayment, AlumniSignUp)

logger = logging.getLogger('date')


class MemberCreationForm(forms.ModelForm):
    send_email = forms.BooleanField(required=False)

    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        min_length=8,
        error_messages={'required': 'Password is required'}
    )

    class Meta:
        model = Member
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'address',
            'zip_code',
            'city',
            'country',
            'membership_type',
            'password',
            'groups',
        )

    def save(self, commit=True):
        member = super(MemberCreationForm, self).save(commit=False)
        member.set_password(self.cleaned_data['password'])
        if commit:
            member.update_or_create(pk=member.pk)
            logger.debug("Saved new member:", member)
        return member


class MemberUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Lösenord",
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = Member
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'address',
            'zip_code',
            'city',
            'country',
            'membership_type',
            'groups',
            'password',
        )

    def save(self, commit=True):
        member = super(MemberUpdateForm, self).save(commit=False)
        password = None
        if password:
            member.set_password(password)
        if commit:
            member.update_or_create(pk=member.pk)
        return member


class SubscriptionPaymentForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPayment
        fields = (
            'member',
            'subscription',
            'date_paid',
            'amount_paid',
        )

    def save(self, commit=True):
        subscription_payment = super(SubscriptionPaymentForm, self).save(commit=False)
        if subscription_payment.subscription.does_expire:
            date_paid = subscription_payment.date_paid
            sub_duration = subscription_payment.subscription.renewal_period
            sub_duration_type = subscription_payment.subscription.renewal_scale
            delta = 0
            if sub_duration_type == SUB_RE_SCALE_DAY:
                delta = relativedelta(days=+sub_duration)
            elif sub_duration_type == SUB_RE_SCALE_MONTH:
                delta = relativedelta(months=+sub_duration)
            elif sub_duration_type == SUB_RE_SCALE_YEAR:
                delta = relativedelta(years=+sub_duration)
            subscription_payment.date_expires = date_paid + delta
            logger.debug("Calculated expiry date for subscription: {}".format(subscription_payment.date_expires))
        if commit:
            subscription_payment.update_or_create(pk=subscription_payment.pk)
            logger.debug("SubscriptionPayment saved")
        return subscription_payment


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=20, help_text='detta fält är obligatoriskt')
    email = forms.EmailField(max_length=200, help_text='detta fält är obligatoriskt')
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        min_length=8,
        error_messages={'required': 'Password is required'},
        help_text='detta fält är obligatoriskt'
    )

    class Meta:
        model = Member
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'address',
            'zip_code',
            'city',
            'country',
            'membership_type',
            'password'
        )


class AlumniSignUpForm(forms.ModelForm):
    tfif_choices = (
        ('ja', 'Ja'),
        ('nej', 'Nej'),
        ('vet inte', 'Vet inte')
    )

    name = forms.CharField(max_length=200, required=True, help_text=_('detta fält är obligatoriskt'), label=_('Namn'))
    email = forms.EmailField(max_length=320, help_text=_('detta fält är obligatoriskt'), label=_('E-postadress'), required=True)
    phone_number = forms.CharField(max_length=20, label=_('Telefonnummer'), required=False)
    address = forms.CharField(max_length=200, label=_('Adress'), required=False)
    year_of_admission = forms.IntegerField(min_value=1900 ,max_value=3000, label=_('Inskrivningsår'), required=False)
    employer = forms.CharField(max_length=200, label=_('Arbetsplats'), required=False)
    work_title = forms.CharField(max_length=200, label=_('Arbetsuppgift'), required=False)
    tfif_membership = forms.ChoiceField(choices=tfif_choices, label=_('TFiF medlemskap'), required=False)
    alumni_newsletter_consent = forms.BooleanField(label=_('Jag tar gärna emot information om alumnevenemang'), required=False)

    class Meta:
        model = AlumniSignUp
        fields = (
            'name',
            'email',
            'phone_number',
            'address',
            'year_of_admission',
            'employer',
            'work_title',
            'tfif_membership',
            'alumni_newsletter_consent',
        )

class SubscriptionPaymentChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if not obj.first_name or not obj.last_name:
            return obj.username
        return f'{obj.first_name} {obj.last_name}'

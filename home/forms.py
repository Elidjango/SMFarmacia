#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'password': forms.PasswordInput()}

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        max_length=64,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Current Password', 'autocomplete': 'off'}))

    new_password = forms.CharField(
        min_length=6,
        max_length=64,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'New Password', 'autocomplete': 'off'}))

    confirm_password = forms.CharField(
        min_length=6,
        max_length=64,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm New Password', 'autocomplete': 'off'}))
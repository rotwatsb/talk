from django.contrib import admin

from .models import Comment, Transaction, TxOut, TxIn, Block

# Register your models here.
admin.site.register(Comment)

admin.site.register(Transaction)

admin.site.register(TxOut)

admin.site.register(TxIn)

admin.site.register(Block)

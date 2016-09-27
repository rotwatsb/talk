from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    block_hash = models.ForeignKey('Block', on_delete=models.CASCADE)

class Transaction(models.Model):
    tx_hash = models.CharField(max_length=64, primary_key=True)
    block_hash = models.ForeignKey('Block', on_delete=models.CASCADE)

class TxOut(models.Model):
    tx = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    output_index = models.IntegerField()
    value = models.BigIntegerField()

class TxIn(models.Model):
    tx = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    prev_tx = models.ForeignKey('Transaction', null=True, on_delete=models.SET_NULL, related_name='input_transaction_set')
    prev_index = models.IntegerField(null=True)
    
class Block(models.Model):
    block_hash = models.CharField(max_length=64, primary_key=True)
    prev_block_hash = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    block_size = models.PositiveIntegerField()
    block_height = models.PositiveIntegerField()
    merkleroot = models.CharField(max_length=64)
    time = models.PositiveIntegerField()
    median_time = models.PositiveIntegerField()
    bits = models.BigIntegerField()
    nonce = models.BigIntegerField()
    

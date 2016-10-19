from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    block_hash = models.ForeignKey('Block', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comment_text)

class Transaction(models.Model):
    tx_hash = models.CharField(max_length=64, primary_key=True)
    block_hash = models.ForeignKey('Block', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tx_hash)

class TxOut(models.Model):
    tx = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    pubkey = models.CharField(max_length=34, null=True)
    output_index = models.IntegerField()
    value = models.BigIntegerField()

    def __str__(self):
        return '_'.join([str(self.tx), str(self.output_index)])

class TxIn(models.Model):
    tx = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    prev_tx = models.CharField(max_length=64, null=True)
    prev_index = models.IntegerField(null=True)

    def __str__(self):
        return '_'.join([str(self.prev_tx), str(self.prev_index)])
    
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

    def __str__(self):
        return str(self.block_hash)
    

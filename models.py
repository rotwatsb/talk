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
    total_value = models.BigIntegerField(null=True, default = None);

    def __str__(self):
        return str(self.tx_hash)

class TxOut(models.Model):
    output = models.CharField(max_length=69, primary_key=True)
    tx = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    address = models.ForeignKey('Address', null=True, on_delete=models.SET_NULL)
    output_index = models.IntegerField()
    value = models.BigIntegerField()

    def __str__(self):
        return str(self.output)

class TxIn(models.Model):
    tx = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    output = models.ForeignKey('TxOut', null=True, on_delete=models.SET_NULL)
        
    def __str__(self):
        return str(self.output)

class Address(models.Model):
    address = models.CharField(max_length=34, primary_key=True)

    def __str__(self):
        return str(self.address)
    
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
    total_value = models.BigIntegerField(null = True, default = None);
    
    def __str__(self):
        return str(self.block_hash)
    

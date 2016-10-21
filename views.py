from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

#from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from .models import Comment, Block, Transaction, TxIn

def index(request):
    #info = rpc_connection.getinfo()
    #best_block_hash = rpc_connection.getbestblockhash()
    info = {}
    info['blocks'] = Block.objects.order_by('-time')
    return render(request, 'talk/index.html', info)

def block_detail(request, block_hash):
    block = get_object_or_404(Block, pk=block_hash)
    block_comments = list(Comment.objects.filter(block_hash=block_hash))
    prev_block_set = block.block_set.all()
    info = {}
    if prev_block_set:
        info['next_block_hash'] = prev_block_set[0].block_hash
    else:
        info['next_block_hash'] = None
    if block.prev_block_hash:
        info['prev_block_hash'] = block.prev_block_hash.block_hash
    else:
        info['prev_block_hash'] = None
        
    info['block_hash'] = block.block_hash
    info['block_height'] = block.block_height
    info['merkleroot'] = block.merkleroot
    info['time'] = block.time
    info['bits'] = block.bits
    info['nonce'] = block.nonce
    info['comments'] = block_comments
    info['transactions'] = block.transaction_set.all()
    
    return render(request, 'talk/block_detail.html', info)

def transaction_detail(request, tx_hash):
    transaction = get_object_or_404(Transaction, pk=tx_hash)
    inputs = transaction.txin_set.exclude(output=None)
    outputs = transaction.txout_set.all()

    def next_tx_or_none(tx_out):
        try:
            return TxIn.objects.get(output=tx_out).tx
        except ObjectDoesNotExist:
            return None
        
    reinputs = [next_tx_or_none(output) for output in outputs]
    info = {}
    info['transaction'] = transaction
    info['inputs'] = inputs
    info['outputs'] = zip(outputs, reinputs)

    return render(request, 'talk/transaction_detail.html', info)
    
def block_post(request, block_hash):
    try:
        comment_text = request.POST['comment'];
    except (KeyError, Comment.DoesNotExist):
        block_detail(request, block_hash)
    else:
        comment = Comment(comment_text=comment_text, block_hash=Block.objects.get(pk=block_hash))
        comment.save()
        return HttpResponseRedirect(reverse('talk:block_detail', args=(block_hash,)))

    

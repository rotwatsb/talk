from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

#from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from .models import Comment, Block, Transaction

#rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("steve", "r3yexx6D"))

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
        
    info['block'] = block
    info['comments'] = block_comments
    info['transactions'] = block.transaction_set.all()
    
    return render(request, 'talk/block_detail.html', info)

def transaction_detail(request, tx_hash):
    transaction = get_object_or_404(Transaction, pk=tx_hash)
    inputs = transaction.txin_set.all()
    outputs = transaction.txout_set.all()
    info = {}
    info['transaction'] = transaction
    info['inputs'] = inputs
    info['outputs'] = outputs

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

    

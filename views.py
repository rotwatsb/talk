from django.http import HttpResponse, Http404

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from django.shortcuts import render


rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("steve", "r3yexx6D"))

def index(request):
    info = rpc_connection.getinfo()
    best_block_hash = rpc_connection.getbestblockhash()
    info['best_block'] = best_block_hash
    return render(request, 'talk/index.html', info)

def block_detail(request, block_hash):
    try:
        block = rpc_connection.getblock(block_hash)
    except JSONRPCException:
        raise Http404("Block not found")
    return render(request, 'talk/block_detail.html', block)
    

    

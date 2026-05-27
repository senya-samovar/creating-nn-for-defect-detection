from IPython import get_ipython
if get_ipython():
    get_ipython().kernel.do_shutdown(restart=True)
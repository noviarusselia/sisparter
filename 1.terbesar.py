#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import mpi4y
from mpi4py import MPI
#buat COMM
comm = MPI.COMM_WORLD
#dapatkan rank proses
rank = comm.Get_rank()
#dapatkan total proses berjalan
size = comm.Get_size()
#jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == size-1:
    data = 'data terbesar'
    for i in range(0, size-1):
        comm.send(data, dest=i)
        print('Proses dengan rank {} mengirim "{}" ke proses dengan rank {}'.format(rank, data, i))
#jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    data = comm.recv(source=size-1)
    print('Proses dengan rank {} menerima "{}" dari proses dengan rank {}'.format(rank, data, size-1))


# In[ ]:





# In[ ]:





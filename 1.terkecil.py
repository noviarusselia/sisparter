#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import mpi4py
from mpi4py import MPI
#buat COMM
comm = MPI.COMM_WORLD
#dapatkan rank proses
rank = comm.Get_rank()
#dapatkan total proses berjalan
size = comm.Get_size()
#jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    data = 'data terkecil'
    for i in range(1, size):
        comm.send(data, dest=i)
        print('Proses {} kirim "{}" ke proses dengan rank {}'.format(rank, data, i))
#jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    data = comm.recv(source=0)
    print('Proses {} menerima "{}" dari proses dengan rank 0'.format(rank, data))


# In[ ]:





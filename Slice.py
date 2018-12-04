#slicing Allows access to one or more elementes in the seqeunce
#Immutable Seqeunce Type
a_tuple=('a',1,2,(3,4))
a_string='immutable'
a_bytes=b'sequence'

#Mutable Seqeunce Type
a_list=[5,6,7,8,(3,4)]
a_byte_array=bytearray(a_bytes)

print(a_byte_array)
#Accessing allowed in all seqeunce
print('a_Tuple[0]->',a_tuple[0])
print('a_string[1]->',a_string[1])
print('a_bytes[2]->',a_bytes[2])
print('a_list[3]->',a_list[3])
print('a_byte_array[4]->',a_byte_array[4])

#Negative Indexes from end
print('a_Tuple[-1]->',a_tuple[-1])
print('a_string[-2]->',a_string[-2])
print('a_bytes[-3]->',a_bytes[-3])
print('a_list[-4]->',a_list[-4])
print('a_byte_array[-5]->',a_byte_array[-5])


#Subslice between two indexes

#first and ignore the last value
print(a_tuple[0:2])
print(a_string[:2])
print(a_string[2:7])
print(a_string[2:])
print(a_list[:])


#use Additional Seqeunce to Access another seqeunce

print(a_tuple) 

import ctypes


class DynamicArray():
    def __init__(self):

        self.n = 0  # Length of A array
        self.capacity = 1  # How many items can A array have
        self.A = self.make_array(self.capacity) # Initializing A array with 1 cell

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n: # if k is equal to or greater than 
            return IndexError("K out of bounds!")

        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity: # if the number of items in the array is equal to the capacity, then we resize the array.
            self._resize(2 * self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap) # Here we create the temp array with the new capacity, 2 * the old capacity

        # Iterate through all items in A and assign them to B.
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)() # Creating memory space with the help of ctypes



a = DynamicArray()
a.append(1)
print(len(a))
a.append(2)
print(len(a))
a.append(3)
print(len(a))        
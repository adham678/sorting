import time
import random
import matplotlib.pyplot as plt
#1

def generate_randomarray(n):
    arr=[]
    for i in range(0,n,1):
        arr.append(random.randint(1,1000000))
    return arr
    
def insertion_sort(arr) :
     start = time.time()
     for i in range(0,len(arr)-1) :
           if(arr[i+1]<arr[i]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                else :
                    break 
     end =time.time()
     print(f"Running time for Insertion Sort is {round((end-start)*1000,5)} ms")
     return round((end-start)*1000,5)

def bubble_sort(arr):
    start=time.time()
    n=len(arr)
    for i in range(1,n):
        sorted =True
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sorted = False
        if sorted:
            break  
    end=time.time()
    print(f"Running time for Bubble Sort is {round((end-start)*1000,5)} ms")           
    return round((end-start)*1000,5)


def selection_sort(arr):
    start=time.time()
    n = len(arr)
    for i in range (n-1):
        min_value = i
        for j in range(i+1,n):
            if arr[min_value]>arr[j]:
                min_value=j
        arr [i],arr[min_value]=arr[min_value],arr[i]

    end = time.time()
    print(f"Running time for selection Sort is {round((end - start) * 1000, 5)} ms")
    return round((end - start) * 1000, 5)

def main():

    ##x=[10000,25000,50000,100000]
    x=[1000,2000,5000,10000]


    

    ##arr1 = generate_randomarray(10000)
    ##arr2 = generate_randomarray(25000)
    ##arr3 = generate_randomarray(50000)
    ##arr4 = generate_randomarray(100000)

    arr1 = generate_randomarray(1000)
    arr2 = generate_randomarray(2000)
    arr3 = generate_randomarray(5000)
    arr4 = generate_randomarray(10000)

    y1i=insertion_sort(arr1.copy())
    y2i=insertion_sort(arr2.copy())
    y3i=insertion_sort(arr3.copy())
    y4i=insertion_sort(arr4.copy())
    yi= [y1i,y2i,y3i,y4i]

    y1s=selection_sort(arr1.copy())
    y2s=selection_sort(arr2.copy())
    y3s=selection_sort(arr3.copy())
    y4s=selection_sort(arr4.copy())
    ys=[y1s,y2s,y3s,y4s]

    y1b=bubble_sort(arr1.copy())
    y2b=bubble_sort(arr2.copy())
    y3b=bubble_sort(arr3.copy())
    y4b=bubble_sort(arr4.copy())
    yb=[y1b,y2b,y3b,y4b]


    plt.plot(x, yi, label='insertion sort', color='yellow', linestyle='-', marker='o')
    plt.plot(x, ys, label='selection sort', color='red', linestyle='-', marker='o')
    plt.plot(x, yb, label='bubble sort', color='blue', linestyle='-', marker='o')
    

    plt.grid(True)

    plt.xlabel('input size (N)')
    plt.ylabel('Execution time(ms)')
    plt.title('(example graph)')

    plt.legend()
    plt.show()




   

if __name__ == "__main__":
    main()               
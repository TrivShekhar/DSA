import java.util.Iterator;

class DynamicArray<T> implements Iterable<T>{
    T arr[];
    int capacity=0;
    int len=0;
    public DynamicArray(){
        this(16);
    }
    public DynamicArray(int capacity){
        if(capacity<0){
            throw new IllegalArgumentException("Illeagal value of capacity"+capacity);
        }
        else{
            arr = (T[]) new Object[capacity];
            this.capacity = capacity;
        }
    }
    public int getCapacity(){
        return this.capacity;
    }
    public int getLen(){
        return this.len;
    }
    public void addElement(T data){
        if(len+1>capacity){
            this.capacity = this.capacity*2;
            T[] arr = (T[]) new Object[capacity];
            for(int i=0;i<len+1;i++){
                arr[i]=this.arr[i];
            }
            arr[len]=data;
            len++;
            this.arr = arr;
        }
        else{
            this.arr[len]=data;
            len++;
        }
    }
    public void removeElement(int index){
        if(index>0 && index<=len){
            T[] arr = (T[]) new Object[capacity-1];
            for(int i =0;i<len;i++){
                if(i>index){
                    arr[i-1]=this.arr[i];
                }
                else{
                    arr[i]=this.arr[i];
                }
            }
        }
        else{
            System.out.println("Element does not exist");
        }
    }
    public void printArr(){
        for(int i=0;i<len;i++){
            System.out.println(this.arr[i]+" ");
        }
    }
    @Override
    public Iterator<T> iterator() {
        // TODO Auto-generated method stub
        return null;
    }
    public static void main(String[] args) {
        DynamicArray<Integer> a = new DynamicArray<Integer>(3);
        a.addElement(5);
        System.out.println(a.getCapacity());
        System.out.println(a.getLen());
        a.addElement(65);
        System.out.println(a.getCapacity());
        System.out.println(a.getLen());
        a.addElement(67);
        System.out.println(a.getCapacity());
        System.out.println(a.getLen());
        a.printArr();
    }
    
}
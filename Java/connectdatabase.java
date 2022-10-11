class some extends Thread{
    public void run(){
        while(true){
            System.out.println(100);;
        }
    }

}

public class connectdatabase  extends Thread{
    public void run(){
        for(int i=0;i<1000;i++){
            System.out.println(i);
        }
    }


    public static void main(String[] args) throws ClassNotFoundException {
       Thread t1=  new some();
       Thread t2= new connectdatabase();
       t1.setDaemon(true);
       t1.start();
       t2.start();
    
}
}

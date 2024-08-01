import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

 public class Main {
   public static void main(String[] args) throws NumberFormatException, IOException {
    
     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

     StringTokenizer st = new StringTokenizer(br.readLine());
     
     int N = Integer.parseInt(st.nextToken());
     
     int X = Integer.parseInt(st.nextToken());

     int[] A = new int[N];
     
     st = new StringTokenizer(br.readLine());
     
     for (int i = 0; i < N; i++){
       A[i] = Integer.parseInt(st.nextToken());
     }

     for (int i = 0; i < N; i++) {
       if (A[i] < X) {
         System.out.print(A[i] + " ");
       }
     }
   }
 }
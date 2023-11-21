public class Solution {
    public static int maxChunksToSorted(int[] arr) {
        int res = 1;
        for(int i = 0; i< arr.length; i++){
            if(LeftMax(arr, i) <= RightMin(arr, i+1))
                res ++;
        }
        return res;
    }

    public static int LeftMax(int[] arr, int t){
        int max = arr[0];
        for(int i = 0; i<= t; i++){
            if(max < arr[i]){
                max = arr[i];
            }
        }
        return max;
    }

    public static int RightMin(int[] arr, int t){
        if(t>=arr.length)
            return -1;
        int min = arr[t];
        for(int i = t; i< arr.length; i++){
            if(min > arr[i]){
                min = arr[i];
            }
        }
        return min;
    }

    public static void main(String[] args) {
        int[] arr = {2,1,3,4,4};
        System.out.println(maxChunksToSorted(arr));
    }
}

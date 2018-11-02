/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int a = 0;
        int b = n;
        int mid;
        while (a < b){
            mid = a/2 + b/2; //使用(a+b)/2会有溢出
            if (isBadVersion(mid)){
                b = mid;
            }else {
                a = mid + 1;
            }
        }
        return a;
    }
}
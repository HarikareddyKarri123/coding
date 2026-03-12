class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count=0;
        int n=jewels.length();
        int m=stones.length();
        for(int i=0;i<n;i++){
            char je=jewels.charAt(i);
            for(int j=0;j<m;j++){
                char s=stones.charAt(j);
                if(je==s){
                    count++;
                }
            }
        }
        return count;
    }
}
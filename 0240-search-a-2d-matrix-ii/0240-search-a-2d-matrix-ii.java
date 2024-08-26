class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Iterate over each element in the matrix
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                // Check if the current element is equal to the target
                if (matrix[i][j] == target) {
                    return true; // Return true if target is found
                }
            }
        }
        // Return false if the target is not found after checking all elements
        return false;
    }
}


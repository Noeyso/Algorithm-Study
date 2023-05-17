function rotate_matrix(matrix){
  const rowLen = matrix.length;
  const colLen = matrix[0].length;

  let rotatedMatrix = [];
  for(let i=0;i<colLen;i++){
    const row = Array(rowLen).fill(0);
    rotatedMatrix.push(row);
  }

  for(let r=0;r<rowLen;r++){
    for(let c=0;c<colLen;c++){
      rotatedMatrix[c][rowLen-r-1] = matrix[r][c];
    }
  }
  return rotatedMatrix;
}


console.log(
  rotate_matrix(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
));
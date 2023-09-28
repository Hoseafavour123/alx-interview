""" Returns a list of lists of integers representing the Pascal's Triangle """

def pascal_triangle(n):
    """_summary_

    Args:
        n (int): number of rows
    """
    
    pascal_tri = [[1], [1, 1]]
    
    if n <= 0:
        return [[]]
    elif n == 1:
        return [pascal_tri[0]]
    elif n == 2:
        return pascal_tri
    
    if n > 2:
        tmp = [1]
        for i in range(n - 2):
            tmp = [1]
            
            for j in range(1, len(pascal_tri[-1])):
                num = (pascal_tri[-1][j - 1] + pascal_tri[-1][j])
                tmp.append(num)
                
            tmp.append(1)
            pascal_tri.append(tmp)
            
        return pascal_tri
            
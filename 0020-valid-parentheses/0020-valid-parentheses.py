class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if (i=='(' or i=='[' or i=='{'):
                st.append(i)
            else:
                if len(st)==0:
                    return False
                el=st[-1]
                st.pop()
                if el=='(' and i==')' or el=='[' and i==']' or el=='{' and i=='}':
                    continue
                else:
                    return False
        
        if len(st)==0:
            return True
        else:
            return False

                


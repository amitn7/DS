def anagram(t,s):
	result = []
	y = "".join(sorted(t))
	for i in xrange(len(s)-len(t)+1):
		x = "".join(sorted(s[i:i+len(t)]))
		if x==y:
			#yield i
			result.append(i)
	yield result
	
def anagram2(s,t):

	countMap,l,r,result,count,j =  {},len(s),len(t),[],0,0	
	for letter in s:
		if letter in countMap.keys():
			countMap[letter]+=1
		else :
			countMap[letter] = 1
	#countMap2 = dict.fromkeys(countMap.keys(),0)
	countMap2 = dict(zip[countMap.keys()],[0])
	#countMap2={letter:0 for letter in countMap.keys()}
	for item,values in countMap2.items():
		print(item,"  ",values)
	if (l>r):
		return result
		
	for i in xrange(l):
		if t[i] in countMap2.keys():
			if countMap2[t[i]]<countMap[t[i]]:
				count+=1
			countMap2[t[i]]+=1	
	if count == l:
		result.append(0)
	j=0
	for i in xrange(l,r):
	
		if t[j] in countMap2.keys():
			if countMap2[t[j]]<=countMap[t[j]]:
				count-=1
			countMap2[t[j]]-=1
		j+=1
		
		if t[i] in countMap2.keys():
			if countMap2[t[i]]<countMap[t[i]]: 
				count+=1
			countMap2[t[i]]+=1
			
		if count==l:
			result.append(j)
		
	
	for num in result:
		print(num)
if __name__=='__main__':
	anagram2("cab","aaabcabdefbacdeabc")
    
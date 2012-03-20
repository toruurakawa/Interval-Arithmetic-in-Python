import math

def pred(a):
    al = abs(a) * pow(2,-53) + pow(2, -55)
    a = a - al
    return a

def succ(a):
    al = abs(a) * pow(2,-53) + pow(2,-55)
    a = a + al
    return a

def TwoSum(a,b):
    x = a + b
    z = x - a
    y = (a - (x - z)) + (b - z)
    return x,y


def Split(a): 
    c = (pow(2,27) + 1) * a
    d = c-a
    x = c - d
    y = a - x
    return x,y

def TwoProduct(a,b):
    a1,a2 = Split(a)
    b1,b2 = Split(b)
    x = a*b
    y = a2*b2 - (((x - a1*b1)-a2*b1)-a1*b2)
    return x,y


class Intv:
    def __init__ (self, low, high):
        if(low == high):
            self.l = self.h = float(low)
        elif(low < high):
            self.l = float(low)
      	    self.h = float(high)
        else:
            self.l = float(high)
            self.h = float(low)
     
    def __repr__(self):
	return "("+repr(self.l)+", "+repr(self.h)+")"
    
    def __add__ (self, other):
        (addl, addle) = TwoSum(self.l, other.l) 
	(addh, addhe) = TwoSum(self.h, other.h)

	if(addle < 0.): addl = pred(addl)
	if(addhe > 0.): addh = succ(addh)

	return Intv(addl, addh)
 
    def __sub__ (self, other):
        (subl, suble) = TwoSum(self.l, -1.0*other.h) 
	(subh, subhe) = TwoSum(self.h, -1.0*other.l)

	if(suble < 0.): subl = pred(subl)
	if(subhe > 0.): subh = succ(subh)

	return Intv(subl, subh)
 

    def __mul__(self, other):
	if((self.l>=0.)and(self.h>=0.)):
	    if((other.l>=0.)and(other.h >=0.)):
 	        ml,mle = TwoProduct(self.l, other.l)
		mh,mhe = TwoProduct(self.h, other.h)
	    
        elif((other.l<0.)and(other.h>=0.)):
		ml,mle = TwoProduct(self.h, other.l)
		mh,mhe = TwoProduct(self.h, other.h)
	    
        elif((other.l<=0.)and(other.h<=0.)):
		ml,mle = TwoProduct(self.h, other.l)
		mh,mhe = TwoProduct(self.l, other.h)
	elif((self.l<0.)and(self.h>=0.)):
	    
        if((other.l>=0.)and(other.h >=0.)):
 	        ml,mle = TwoProduct(self.l, other.h)
		mh,mhe = TwoProduct(self.h, other.h)
	   
        elif((other.l<0.)and(other.h>=0.)):
		ml1,ml1e = TwoProduct(self.l, other.h)
		ml2,ml2e = TwoProduct(self.h, other.l)
                if(ml1<ml2):
	            ml = ml1
    	            mle = ml1e
                elif(ml1>ml2):
	            ml = ml2
		    mle = ml2e
		else:
		    if(ml1e<ml2e):
			ml = ml1
		 	mle = ml1e
	            else:
			ml = ml2
			mle = ml2e
	        mh1,mh1e = TwoProduct(self.l, other.l)
		mh2,mh2e = TwoProduct(self.h, other.h)
	        if(mh1>mh2):
	            mh = mh1
    	            mhe = mh1e
                elif(mh1<mh2):
	            mh = mh2
		    mhe = mh2e
		else:
		    if(mh1e>mh2e):
			mh = mh1
		 	mhe = mh1e
	            else:
			mh = mh2
			mhe = mh2e
	     elif((other.l<=0.)and(other.h<=0.)):
		ml,mle = TwoProduct(self.h, other.l)
		mh,mhe = TwoProduct(self.l, other.l)
	elif((self.l<=0.)and(self.h<=0.)):
	     if((other.l>=0.)and(other.h >=0.)):
 	        ml,mle = TwoProduct(self.l, other.h)
		mh,mhe = TwoProduct(self.h, other.l)
	     elif((other.l<0.)and(other.h>=0.)):
		ml,mle = TwoProduct(self.l, other.h)
		mh,mhe = TwoProduct(self.l, other.l)
	     elif((other.l<=0.)and(other.h<=0.)):
		ml,mle = TwoProduct(self.h, other.h)
		mh,mhe = TwoProduct(self.l, other.l)	

	if(mle < 0.):ml = pred(ml)
	if(mhe > 0.):mh = succ(mh)
	
        return Intv(ml, mh)

    def __div__(self, other):
	if((self.l>=0.)and(self.h>=0.)):
	    if((other.l>=0.)and(other.h>=0.)):	
	        #low
                cl = self.l/other.h
	        al,ale = TwoProduct(cl,other.h)
	        if(al>self.l): 
		    cl = pred(cl)
		elif(al==self.l):
		    if(ale > 0.):
			cl = pred(cl)
		    	
	        #high
		ch = self.h/other.h
                ah,ahe = TwoProduct(ch,other.h)
	        if(ah<self.h): 
		    ch = succ(ch)
		elif(ah==self.h):
		    if(ahe < 0.):
		        ch = succ(ch)

            elif((other.l<=0.)and(other.h<=0.)):	
	        #low
                cl = self.h/other.h
	        al,ale = TwoProduct(cl,other.h)
	        if(al>self.h): 
		    cl = pred(cl)
		elif(al==self.h):
		    if(ale > 0.):
			cl = pred(cl)
		    	
	        #high
		ch = self.l/other.l
                ah,ahe = TwoProduct(ch,other.l)
	        if(ah<self.l): 
		    ch = succ(ch)
		elif(ah==self.l):
		    if(ahe < 0.):
		        ch = succ(ch)
        
	elif((self.l<0.)and(self.h>=0.)):
           if((other.l>=0.)and(other.h>=0.)):	
	        #low
                cl = self.l/other.l
	        al,ale = TwoProduct(cl,other.l)
	        if(al>self.l): 
		    cl = pred(cl)
		elif(al==self.l):
		    if(ale > 0.):
			cl = pred(cl)
		    	
	        #high
		ch = self.h/other.l
                ah,ahe = TwoProduct(ch,other.l)
	        if(ah<self.h): 
		    ch = succ(ch)
		elif(ah==self.h):
		    if(ahe < 0.):
		        ch = succ(ch)
           elif((other.l<=0.)and(other.h<=0.)):	
	        #low
                cl = self.h/other.h
	        al,ale = TwoProduct(cl,other.h)
	        if(al>self.h): 
		    cl = pred(cl)
		elif(al==self.h):
		    if(ale > 0.):
			cl = pred(cl)
		    	
	        #high
		ch = self.l/other.h
                ah,ahe = TwoProduct(ch,other.h)
	        if(ah<self.l): 
		    ch = succ(ch)
		elif(ah==self.l):
		    if(ahe < 0.):
		        ch = succ(ch)
   
        elif((self.l<=0.)and(self.h<=0.)):        
	   if((other.l>=0.)and(other.h>=0.)):	
		#low
                cl = self.l/other.l
	        al,ale = TwoProduct(cl,other.l)
	        if(al>self.l): 
		    cl = pred(cl)
		elif(al==self.l):
		    if(ale > 0.):
			cl = pred(cl)
		    	
	        #high
		ch = self.h/other.h
                ah,ahe = TwoProduct(ch,other.h)
	        if(ah<self.h): 
		    ch = succ(ch)
		elif(ah==self.h):
		    if(ahe < 0.):
		        ch = succ(ch)

           elif((other.l<=0.)and(other.h<=0.)):	
	 	#low
                cl = self.h/other.l
	        al,ale = TwoProduct(cl,other.l)
	        if(al>self.h): 
		    cl = pred(cl)
		elif(al==self.h):
		    if(ale > 0.):
			cl = pred(cl)
		    	
	        #high
		ch = self.l/other.h
                ah,ahe = TwoProduct(ch,other.h)
	        if(ah<self.l): 
		    ch = succ(ch)
		elif(ah==self.l):
		    if(ahe < 0.):
		        ch = succ(ch)

	return Intv(cl, ch)
        

def intvSqrt(a):
    ral = math.sqrt(a.l)
    rah = math.sqrt(a.h)
    
    al,ale = TwoProduct(ral,ral)
    if(al>a.l): ral = pred(ral)

    ah,ahe = TwoProduct(rah,rah)
    if(ah<a.h): rah = succ(rah)

    return Intv(ral, rah)


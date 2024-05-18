import cv2
from PIL import Image
import numpy
def converFullBin(val,bit):
    bins=bin(val)
    bins=bins[2:len(bins)]
    while len(bins)!=bit:
        bins="0"+bins
    return bins

def text2Bin(st):
    binary=""
    for i in st:
         binary=binary+converFullBin(ord(i),8)
    
    return binary

def bin2Text(st):
    ans=""
    total_bit=len(st)
    total_char=total_bit//8
    j=0
    for i in range(total_char):
        part=st[j:j+8]
        j+=8
        ch=int(part,2)
        ans=ans+chr(ch)
    return ans
def image2Bin(s,password):
    s=cv2.imread(s)
    total_loop_num=96
    loop_num=1
    i_value=len(s)
    j_value=len(s[0])
    flag=True
    ans=""
    for i in range(i_value):
        if flag:
            for j in range(j_value):
                if flag:
                    for k in range(3):
                        n=s[i][j][k]
                        bina=converFullBin(n,8)
                        # print(bina)
                        ans=ans+bina[7:8]
                        if loop_num==total_loop_num:
                            flag=False
                            break
                        loop_num=loop_num+1
    flag=bin2Text(ans[0:8])
    size=int(ans[8:32],2)
    passGive=bin2Text(ans[32:96])
    if passGive==password:
        size=size*8
        total_loop_num=(96+size)
        loop_num=1
        i_value=len(s)
        j_value=len(s[0])
        flag=True
        ans=""
        for i in range(i_value):
            if flag:
                for j in range(j_value):
                    if flag:
                        for k in range(3):
                            n=s[i][j][k]
                            bina=converFullBin(n,8)
                            ans=ans+bina[7:8]
                            if loop_num==total_loop_num:
                                flag=False
                                break
                            loop_num=loop_num+1
        msg=bin2Text(ans[96:(size*8)])
        return msg
    else:
        return "-1"
    
 
def encode(text,passw,files,dest):
    arr=cv2.imread(files)
    s=arr
    pass_bin=text2Bin(passw)
    length_bin=converFullBin(len(text),24)
    flag=text2Bin("T")
    text_bin=text2Bin(text)
    total_bin=flag+length_bin+pass_bin+text_bin
    # total_bin=text_bin
    # print(total_bin)
    total_loop_num=len(total_bin)
    loop_num=1
    i_value=len(s)
    j_value=len(s[0])
    ans=""
    for i in range(i_value):
        for j in range(j_value):
            for k in range(3):
                temp=s[i][j][k]
                temp=converFullBin(temp,8)
                temp=temp[0:7]+total_bin[((loop_num*1)-1):(loop_num*1)]
                s[i][j][k]=int(temp,2)
                if loop_num==total_loop_num:
                    break
                loop_num=loop_num+1
            if loop_num==total_loop_num:
                    break
        if loop_num==total_loop_num:
                    break
    
    cv2.imwrite(dest, s)
        


# if __name__ == "__main__":
#     print("Press 1 for encode text in photo")
#     print("Press 2 for decode text from photo")
#     choice=int(input("Enter Your Choice:"))
#     if choice==1:
#         files=input("Enter name of the image for encoding with extension(Ex:test.jpg):")
#         text=input("Enter your message:")
#         password=input("Enter a 8 character password:")
#         arr=cv2.imread(files)
#         arr=encode(arr,text,password)
#         files_out=files.split('.')[0] +'_modified.png'
#         cv2.imwrite(files_out, arr)
#         print("Your image have been saved by "+files_out+" name")
        
#     elif choice==2:
#         files=input("Enter name of the image to for decoding with extention(Ex:test.jpg):")
#         arr=cv2.imread(files)
#         passd=input("Enter the password:")
#         msg=image2Bin(arr,passd)
#         print(msg)
    


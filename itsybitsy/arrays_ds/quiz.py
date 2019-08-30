# # a_list = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 100, 115, 119, 107, 102, 119, 50, 51, 119, 48, 101, 107, 101, 103, 101, 102, 103 ]
a_list = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 119, 101, 102, 102, 107, 102, 112, 102, 108, 101, 109, 115, 105, 115, 111, 100, 100 ]
a_list = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 103, 103, 112, 100, 103, 108, 100, 103, 45, 54, 116, 121, 45, 100, 115, 115 ]
print(''.join(chr(i) for i in a_list))
#

from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
# message = b'gAAAAABctBegNTcgOvE8KCgJ4UbciOGDcotUzk8EvmVB0ie5M4Rs_w_dIsSuqAEQvhiYmm9JyJKT6CG9XsjyJKDKMum1WNaNrvc8gSV55s7e7sRzOTRbzNxqNXFBUoeW4CdWeeVHg07kMufo6CxNieL1_1JdImLJ_EFN_Za6sE3nen-C5yMnaKM='
# message = b'gAAAAABdSvis-j6vwofrJi-6dzrQDgbKCmDZZcxPbv2l66W7QG_YTebGgu-Br3DHi5BtZiFSsKI-1DGiOP113uvMllkSJFZALKXUkqOX0TbwdRt_g8bePNKE-SEKgOVtPCbmhHuw5ldRIK-SFKLjTsZghaFH1YrFKGNL5AQFFC4OaEXAlIczudc='
message = b'gAAAAABdSvrYVSonQwutOYQxrtZVosyaRSku1CwG9n3kk5czOg2XOaFVUyuPnvgJAG5XuJj1snjr_I4G7HYDLzW4uyS3GQ4bArVRa4kjTQDoj1n4ZLRChkTUu3a_qo0kKOLptfY8_Q4zhevNvMGFvFU8zKMRFWRadG2F7_DKBhUGKT7ponfZeQI='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

# https://engineering-application.britecore.com/e/t15e119s3t/testProductEngineer'
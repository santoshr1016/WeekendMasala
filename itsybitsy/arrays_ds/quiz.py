# a_list = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 100, 115, 119, 107, 102, 119, 50, 51, 119, 48, 101, 107, 101, 103, 101, 102, 103 ]
#
# print(''.join(chr(i)for i in a_list))


from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABctBegNTcgOvE8KCgJ4UbciOGDcotUzk8EvmVB0ie5M4Rs_w_dIsSuqAEQvhiYmm9JyJKT6CG9XsjyJKDKMum1WNaNrvc8gSV55s7e7sRzOTRbzNxqNXFBUoeW4CdWeeVHg07kMufo6CxNieL1_1JdImLJ_EFN_Za6sE3nen-C5yMnaKM='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

# https://engineering-application.britecore.com/e/t15e119s3t/testProductEngineer'
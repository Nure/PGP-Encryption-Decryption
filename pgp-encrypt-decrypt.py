import os
import gnupg

def encrypt():
    files_dir = []
    for directory, subdirectory, files_list in os.walk('files'):
        files = [os.path.join(directory, f) for f in files_list]
        for f in files:
            files_dir.append(f)
        for x in files_dir:
            with open(x, "rb") as f:
                status = gpg.encrypt_file(f, recipients=["nalamsiddiq@gmail.com"], output=files_dir[files_dir.index(x)] +
                                                                                        ".pgp", always_trust=True)
                print("ok: ", status.ok)
                print("status: ", status.status)
                print("stderr: ", status.stderr)
def decrypt():
    files_dir = []
    files_dir_clean = []

    for directory, subdirectory, files_list in os.walk('encrypted'):
        files = [os.path.join(directory, f) for f in files_list]
        for f in files:
            files_dir.append(f)

        for x in files_dir:
            length = len(x)
            endLoc = length - 4
            clean_file = x[0:endLoc]
            files_dir_clean.append(clean_file)

        for x in files_dir:
            with open(x, "rb") as f:
                status = gpg.decrypt_file(f, passphrase=my_passphrase, output=files_dir_clean[files_dir.index(x)])
                print("ok: ", status.ok)
                print("status: ", status.status)
                print("stderr: ", status.stderr)

if __name__ == '__main__':
    my_passphrase = 'xygfht'
    key = 'TestPGPpublicKey.asc'
    gpg = gnupg.GPG(gnupghome=".")
    with open(key, 'rb') as f_obj:
        gpg.import_keys(f_obj.read())

    encrypt()

    decrypt()

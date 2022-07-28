{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf755560",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "creater username :abcd@gmail.com\n",
      "Valid email\n",
      "create password :123456!\n",
      "confirm password :123456!\n",
      "password is accepted\n",
      "{'rrttr': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, '214': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, 'asdf@ghma.com': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, 'asdf@gmail.com': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, 'Adad@gmail.com': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, 'adarf': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, 'asadf@ghma.com': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>, 'abcd@gmail.com': <_io.TextIOWrapper name='db.txt' mode='r' encoding='cp1252'>}\n",
      "username esists\n"
     ]
    }
   ],
   "source": [
    "def register():\n",
    "    b=open(\"db.txt\",\"r\")\n",
    "    import re\n",
    "    pattern =\"[a-zA-Z]+@[a-zA-Z]+\\.(com|edu|net)\"\n",
    "    u=input(\"creater username :\")\n",
    "    if (re.search(pattern,u)):\n",
    "        print(\"Valid email\")\n",
    "    else:\n",
    "        print(\"Invalid email\")\n",
    "        register()\n",
    "    pattern2 = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')\n",
    "    p=input(\"create password :\")\n",
    "    p1=input(\"confirm password :\")\n",
    "    if(pattern2.search(p) != None):\n",
    "        print(\"password is accepted\")\n",
    "    else:\n",
    "        print(\"password should contain special character.\")\n",
    "\n",
    "    if p!=p1:\n",
    "        print(\"password doesn't match\")\n",
    "        register()\n",
    "    else:\n",
    "        if len(p)<5:\n",
    "            print(\"password is too short\")\n",
    "        elif len(p)>12:\n",
    "            print(\"Password is too long\")\n",
    "            register()  \n",
    "        elif u in d:\n",
    "            print(\"username esists\")\n",
    "            register()\n",
    "        else:\n",
    "            b=open(\"db.txt\",\"a\")\n",
    "            b.write(u+\",\"+p+\"\\n\")\n",
    "            print(\"login\")\n",
    "register()\n",
    "\n",
    "\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "157a3b51",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db29a047",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "444c56dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42a87029",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

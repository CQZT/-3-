#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�֣����
���ڣ�2020��4��5
"""




#�������裺

    # 0 - ʯͷ # 1 - ʷ���� # 2 - ֽ # 3 - ���� # 4 - ����

    # ���"-------- "���зָ�
    
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    
    
    
    
#����randon����Ⲣ����[0,4]�������    
import random
comp_number=random.randrange(0,5)#randon����������������������޵�����������





#����Ϸ�����Ӧ����ͬ������
def name_to_number(player_choice):
	if player_choice=="ʯͷ":
		return 0
	elif player_choice=='ʷ����':
		return 1
	elif player_choice=='ֽ':
		return 2
	elif player_choice=='����':
		return 3
	elif player_choice=='����':
		return 4





# ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
def number_to_name(comp_number):
	if comp_number==0:
		return 'ʯͷ'
	elif comp_number==1:
		return 'ʷ����'
	elif comp_number==2:
		return 'ֽ'
	elif comp_number==3:
		return '����'
	elif comp_number==4:
		return '����'





#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ�����ж�ʤ��
def rpsls(player_choice):
	if (player_choice_number==0 and (comp_number==3 or comp_number==4)) or (player_choice_number== 1 and (comp_number==0 or comp_number==4)) or (player_choice_number==2 and (comp_number==0 or comp_number==1)) or (player_choice_number==3 and (comp_number==1 or comp_number==2)) or (player_choice_number==4 and (comp_number==3 or comp_number==2)):
		return '��Ӯ��'
	elif (player_choice_number==0 and comp_number==0) or (player_choice_number==1 and comp_number==1) or (player_choice_number==2 and comp_number==2) or (player_choice_number==3 and comp_number==3) or (player_choice_number==4 and comp_number==4):
		return 'ƽ��'
	else:
		return '�����Ӯ��'





#������ú���ʾ
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()#������ҵ�ѡ��
player_choice_number=name_to_number(player_choice)#���ú���name_to_number���õ����ѡ������Ӧ������
comp_number_name=number_to_name(comp_number)#���ú���number_to_name���õ���������������������Ӧ��ѡ��
result=rpsls(player_choice)#���ú���rpsls���õ���Һ͵���ѡ���ʤ��
if player_choice==('ʯͷ' or '����' or '��' or 'ʷ����' or '����'):#��if�����ж���ҵ�ѡ���ǲ���ʯͷ/����/��/ʷ����/�����е�һ��
	print("----------------")
	print("����ѡ��Ϊ:"+player_choice)
	print("�������ѡ��Ϊ:"+comp_number_name)
	print(result)
else:
	print("Error: No Correct Name")

{\rtf1\ansi\ansicpg1251\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red156\green156\blue156;\red255\green255\blue255;\red0\green0\blue0;
\red13\green100\blue117;\red0\green0\blue109;\red15\green112\blue1;\red251\green0\blue7;\red14\green110\blue109;
\red43\green139\blue2;\red0\green0\blue255;\red0\green0\blue213;\red0\green0\blue49;}
{\*\expandedcolortbl;;\cssrgb\c67451\c67451\c67451;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c0\c46667\c53333;\cssrgb\c0\c0\c50196;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c0\c0;\cssrgb\c0\c50196\c50196;
\cssrgb\c20000\c60000\c0;\cssrgb\c0\c0\c100000;\cssrgb\c0\c0\c86667;\cssrgb\c0\c0\c25098;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid1\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f0\fs24 \cf2 \cb3 {\listtext	1	}\expnd0\expndtw0\kerning0
from wtforms import DecimalField, StringField, BooleanField, DateField, SubmitField\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	2	}\expnd0\expndtw0\kerning0
from flask import Flask, render_template, request, redirect, flash\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	3	}\expnd0\expndtw0\kerning0
from flask_mongoengine import MongoEngine, Document\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	4	}\expnd0\expndtw0\kerning0
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	5	}\expnd0\expndtw0\kerning0
from flask_wtf import FlaskForm\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	6	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	7	}\expnd0\expndtw0\kerning0
from mongoengine.\cf5 queryset\cf2 .\cf5 visitor\cf2  import Q\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	8	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	9	}\expnd0\expndtw0\kerning0
app \cf6 =\cf2  Flask\cf7 (\cf2 __name__\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	10	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	11	}\expnd0\expndtw0\kerning0
app.\cf5 config\cf7 [\cf8 'MONGODB_SETTINGS'\cf7 ]\cf2  \cf6 =\cf2  \cf7 \{\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	12	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf8 "db"\cf9 :\cf2  \cf8 "rospatent"\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf7 \kerning1\expnd0\expndtw0 {\listtext	13	}\expnd0\expndtw0\kerning0
\}\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	14	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	15	}\expnd0\expndtw0\kerning0
db \cf6 =\cf2  MongoEngine\cf7 (\cf2 app\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	16	}\expnd0\expndtw0\kerning0
app.\cf5 config\cf7 [\cf8 'SECRET_KEY'\cf7 ]\cf2  \cf6 =\cf2  \cf8 'Trudy'\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	17	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	18	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf10 \kerning1\expnd0\expndtw0 {\listtext	19	}\expnd0\expndtw0\kerning0
# Authorization\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	20	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	21	}\expnd0\expndtw0\kerning0
login_manager \cf6 =\cf2  LoginManager\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	22	}\expnd0\expndtw0\kerning0
login_manager.\cf5 init_app\cf7 (\cf2 app\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	23	}\expnd0\expndtw0\kerning0
login_manager.\cf5 login_view\cf2  \cf6 =\cf2  \cf8 'login'\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	24	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	25	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf11 \kerning1\expnd0\expndtw0 {\listtext	26	}\expnd0\expndtw0\kerning0
class\cf2  User\cf7 (\cf2 UserMixin, db.\cf5 Document\cf7 )\cf9 :\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	27	}\expnd0\expndtw0\kerning0
\'a0 \'a0 meta \cf6 =\cf2  \cf7 \{\cf8 'collection'\cf9 :\cf2  \cf8 'users'\cf7 \}\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	28	}\expnd0\expndtw0\kerning0
\'a0 \'a0 username \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	29	}\expnd0\expndtw0\kerning0
\'a0 \'a0 password \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	30	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	31	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	32	}\expnd0\expndtw0\kerning0
@login_manager.\cf5 user_loader\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	33	}\expnd0\expndtw0\kerning0
def load_user\cf7 (\cf2 user_id\cf7 )\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	34	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 return\cf2  User.\cf5 objects\cf7 (\cf2 pk\cf6 =\cf2 user_id\cf7 )\cf2 .\cf5 first\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	35	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	36	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf10 \kerning1\expnd0\expndtw0 {\listtext	37	}\expnd0\expndtw0\kerning0
# users collection\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	38	}\expnd0\expndtw0\kerning0
User.\cf5 drop_collection\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	39	}\expnd0\expndtw0\kerning0
User\cf7 (\cf2 username\cf6 =\cf8 "admin"\cf2 , password\cf6 =\cf8 "123"\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	40	}\expnd0\expndtw0\kerning0
User\cf7 (\cf2 username\cf6 =\cf8 "chel"\cf2 , password\cf6 =\cf8 "321"\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	41	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	42	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf10 \kerning1\expnd0\expndtw0 {\listtext	43	}\expnd0\expndtw0\kerning0
# Patents db\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	44	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	45	}\expnd0\expndtw0\kerning0
fields \cf6 =\cf2  \cf7 [\cf8 'registration number'\cf2 , \cf8 'registration date'\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	46	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \cf8 'application number'\cf2 , \cf8 'application date'\cf2 , \cf8 'authors'\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	47	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \cf8 'authors count'\cf2 , \cf8 'right holders'\cf2 , \cf8 'contact to third parties'\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	48	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \cf8 'program name'\cf2 , \cf8 'creation year'\cf2 , \cf8 'registration publish date'\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	49	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \cf8 'registration publish number'\cf2 , \cf8 'actual'\cf2 , \cf8 'publication URL'\cf7 ]\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	50	}\expnd0\expndtw0\kerning0
fields_name \cf6 =\cf2  \cf7 [\cf2 field.\cf5 replace\cf7 (\cf8 " "\cf2 , \cf8 "_"\cf7 )\cf2  \cf11 for\cf2  field in fields\cf7 ]\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	51	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	52	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf11 \kerning1\expnd0\expndtw0 {\listtext	53	}\expnd0\expndtw0\kerning0
class\cf2  Patent\cf7 (\cf2 UserMixin, db.\cf5 Document\cf7 )\cf9 :\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	54	}\expnd0\expndtw0\kerning0
\'a0 \'a0 meta \cf6 =\cf2  \cf7 \{\cf8 'collection'\cf9 :\cf2  \cf8 'patents'\cf7 \}\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	55	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_number \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	56	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_date \cf6 =\cf2  db.\cf5 DateField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	57	}\expnd0\expndtw0\kerning0
\'a0 \'a0 application_number \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	58	}\expnd0\expndtw0\kerning0
\'a0 \'a0 application_date \cf6 =\cf2  db.\cf5 DateField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	59	}\expnd0\expndtw0\kerning0
\'a0 \'a0 authors \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	60	}\expnd0\expndtw0\kerning0
\'a0 \'a0 authors_count \cf6 =\cf2  db.\cf5 DecimalField\cf7 (\cf2 precision\cf6 =\cf12 0\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	61	}\expnd0\expndtw0\kerning0
\'a0 \'a0 right_holders \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	62	}\expnd0\expndtw0\kerning0
\'a0 \'a0 contact_to_third_parties \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	63	}\expnd0\expndtw0\kerning0
\'a0 \'a0 program_name \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	64	}\expnd0\expndtw0\kerning0
\'a0 \'a0 creation_year \cf6 =\cf2  db.\cf5 DecimalField\cf7 (\cf2 precision\cf6 =\cf12 0\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	65	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_publish_date \cf6 =\cf2  db.\cf5 DateField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	66	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_publish_number \cf6 =\cf2  db.\cf5 DecimalField\cf7 (\cf2 precision\cf6 =\cf12 0\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	67	}\expnd0\expndtw0\kerning0
\'a0 \'a0 actual \cf6 =\cf2  db.\cf5 BooleanField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	68	}\expnd0\expndtw0\kerning0
\'a0 \'a0 publication_URL \cf6 =\cf2  db.\cf5 StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	69	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	70	}\expnd0\expndtw0\kerning0
\'a0 \'a0 def to_dict\cf7 (\cf2 self\cf7 )\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	71	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 d \cf6 =\cf2  \cf7 \{\}\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	72	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 for\cf2  field in fields\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	73	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 field_name \cf6 =\cf2  field.\cf5 replace\cf7 (\cf8 " "\cf2 , \cf8 "_"\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	74	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 d\cf7 [\cf2 field_name\cf7 ]\cf2  \cf6 =\cf2  str\cf7 (\cf2 self\cf7 [\cf2 field_name\cf7 ])\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	75	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  d\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	76	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	77	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf10 \kerning1\expnd0\expndtw0 {\listtext	78	}\expnd0\expndtw0\kerning0
# patents collection\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	79	}\expnd0\expndtw0\kerning0
Patent.\cf5 drop_collection\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	80	}\expnd0\expndtw0\kerning0
Patent\cf7 (\cf2 registration_number\cf6 =\cf8 "950396"\cf2 , registration_date\cf6 =\cf8 "1995-11-09"\cf2 ,application_number\cf6 =\cf8 "0000950377"\cf2 ,application_date\cf6 =\cf8 "1995-10-19"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	81	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors\cf6 =\cf8 "\uc0\u1058 \u1102 \u1093 \u1086 \u1074  \u1041 \u1086 \u1088 \u1080 \u1089  \u1055 \u1077 \u1090 \u1088 \u1086 \u1074 \u1080 \u1095  (RU) \u1048 \u1083 \u1100 \u1080 \u1095 \u1077 \u1085 \u1082 \u1086 \u1074 \u1072  \u1047 \u1086 \u1103  \u1042 \u1080 \u1082 \u1090 \u1086 \u1088 \u1086 \u1074 \u1085 \u1072  \'a0(RU) \u1060 \u1077 \u1076 \u1086 \u1089 \u1077 \u1077 \u1074 \u1072  \u1058 \u1072 \u1090 \u1100 \u1103 \u1085 \u1072  \u1051 \u1077 \u1086 \u1085 \u1080 \u1076 \u1086 \u1074 \u1085 \u1072  (RU)"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	82	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors_count\cf6 =\cf12 3\cf2 , right_holders\cf6 =\cf8 "\uc0\u1058 \u1102 \u1093 \u1086 \u1074  \u1041 \u1086 \u1088 \u1080 \u1089  \u1055 \u1077 \u1090 \u1088 \u1086 \u1074 \u1080 \u1095  (RU)"\cf2 , contact_to_third_parties\cf6 =\cf8 ""\cf2 ,program_name\cf6 =\cf8 ""\cf2 ,creation_year\cf6 =\cf2 None,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	83	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0registration_publish_date\cf6 =\cf8 "1996-03-20"\cf2 , registration_publish_number\cf6 =\cf12 1\cf2 ,actual\cf6 =\cf2 True,publication_URL\cf6 =\cf8 "http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=950396"\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	84	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	85	}\expnd0\expndtw0\kerning0
Patent\cf7 (\cf2 registration_number\cf6 =\cf8 "970019"\cf2 , registration_date\cf6 =\cf8 "1997-01-17"\cf2 ,application_number\cf6 =\cf8 "0000960509"\cf2 ,application_date\cf6 =\cf8 "1996-12-20"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	86	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors\cf6 =\cf8 "\uc0\u1050 \u1086 \u1083 \u1076 \u1080 \u1085 \u1072  \u1040 .\u1048 . (RU) \u1052 \u1072 \u1082 \u1072 \u1088 \u1086 \u1074  \u1057 .\u1042 . (RU) \u1040 \u1083 \u1077 \u1082 \u1089 \u1072 \u1085 \u1076 \u1088 \u1086 \u1074 \u1072  \u1043 .\u1052 . (RU) \u1048 \u1074 \u1072 \u1085 \u1086 \u1074  \u1042 .\u1043 . (RU) \u1042 \u1099 \u1089 \u1086 \u1094 \u1082 \u1072 \u1103  \u1053 .\u1042 . (RU) \u1051 \u1077 \u1073 \u1077 \u1076 \u1077 \u1074  \u1057 .\u1053 . (RU)"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	87	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors_count\cf6 =\cf12 6\cf2 , right_holders\cf6 =\cf8 "\uc0\u1063 \u1072 \u1088 \u1089 \u1082 \u1080 \u1081  \u1042 \u1080 \u1090 \u1072 \u1083 \u1080 \u1081  \u1042 \u1083 \u1072 \u1076 \u1080 \u1084 \u1080 \u1088 \u1086 \u1074 \u1080 \u1095  (RU) \u1048 \u1074 \u1072 \u1085 \u1086 \u1074  \u1042 \u1083 \u1072 \u1076 \u1080 \u1084 \u1080 \u1088  \u1043 \u1077 \u1086 \u1088 \u1075 \u1080 \u1077 \u1074 \u1080 \u1095  (RU)"\cf2 , contact_to_third_parties\cf6 =\cf8 ""\cf2 ,program_name\cf6 =\cf8 "\uc0\u1050 \u1086 \u1084 \u1087 \u1083 \u1077 \u1082 \u1089 \u1085 \u1072 \u1103  \u1089 \u1080 \u1089 \u1090 \u1077 \u1084 \u1072  \u1080 \u1085 \u1092 \u1086 \u1088 \u1084 \u1072 \u1094 \u1080 \u1086 \u1085 \u1085 \u1086 \u1075 \u1086  \u1086 \u1073 \u1077 \u1089 \u1087 \u1077 \u1095 \u1077 \u1085 \u1080 \u1103  \u1091 \u1095 \u1077 \u1090 \u1072  \u1080  \u1076 \u1074 \u1080 \u1078 \u1077 \u1085 \u1080 \u1103  \u1082 \u1072 \u1076 \u1088 \u1086 \u1074 "\cf2 ,creation_year\cf6 =\cf2 None,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	88	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0registration_publish_date\cf6 =\cf8 "1997-06-20"\cf2 , registration_publish_number\cf6 =\cf12 2\cf2 ,actual\cf6 =\cf2 True,publication_URL\cf6 =\cf8 "http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=970019"\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	89	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	90	}\expnd0\expndtw0\kerning0
Patent\cf7 (\cf2 registration_number\cf6 =\cf8 "950396"\cf2 , registration_date\cf6 =\cf8 "1995-11-09"\cf2 ,application_number\cf6 =\cf8 "19951019"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	91	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors\cf6 =\cf8 "\uc0\u1058 \u1102 \u1093 \u1086 \u1074  \u1041 \u1086 \u1088 \u1080 \u1089  \u1055 \u1077 \u1090 \u1088 \u1086 \u1074 \u1080 \u1095  (RU) \u1048 \u1083 \u1100 \u1080 \u1095 \u1077 \u1085 \u1082 \u1086 \u1074 \u1072  \u1047 \u1086 \u1103  \u1042 \u1080 \u1082 \u1090 \u1086 \u1088 \u1086 \u1074 \u1085 \u1072  \'a0(RU) \u1060 \u1077 \u1076 \u1086 \u1089 \u1077 \u1077 \u1074 \u1072  \u1058 \u1072 \u1090 \u1100 \u1103 \u1085 \u1072  \u1051 \u1077 \u1086 \u1085 \u1080 \u1076 \u1086 \u1074 \u1085 \u1072  (RU)"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	92	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors_count\cf6 =\cf12 3\cf2 , right_holders\cf6 =\cf8 "\uc0\u1058 \u1102 \u1093 \u1086 \u1074  \u1041 \u1086 \u1088 \u1080 \u1089  \u1055 \u1077 \u1090 \u1088 \u1086 \u1074 \u1080 \u1095  (RU)"\cf2 , contact_to_third_parties\cf6 =\cf8 ""\cf2 ,program_name\cf6 =\cf8 ""\cf2 ,creation_year\cf6 =\cf2 None,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	93	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0registration_publish_date\cf6 =\cf8 "1996-03-20"\cf2 , registration_publish_number\cf6 =\cf12 1\cf2 ,actual\cf6 =\cf2 True,publication_URL\cf6 =\cf8 "http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=950396"\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	94	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	95	}\expnd0\expndtw0\kerning0
Patent\cf7 (\cf2 registration_number\cf6 =\cf8 "970019"\cf2 , registration_date\cf6 =\cf8 "1997-01-17"\cf2 ,application_number\cf6 =\cf8 "0000960509"\cf2 ,application_date\cf6 =\cf8 "1996-12-20"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	96	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors\cf6 =\cf8 "\uc0\u1050 \u1086 \u1083 \u1076 \u1080 \u1085 \u1072  \u1040 .\u1048 . (RU) \u1052 \u1072 \u1082 \u1072 \u1088 \u1086 \u1074  \u1057 .\u1042 . (RU) \u1040 \u1083 \u1077 \u1082 \u1089 \u1072 \u1085 \u1076 \u1088 \u1086 \u1074 \u1072  \u1043 .\u1052 . (RU) \u1048 \u1074 \u1072 \u1085 \u1086 \u1074  \u1042 .\u1043 . (RU) \u1042 \u1099 \u1089 \u1086 \u1094 \u1082 \u1072 \u1103  \u1053 .\u1042 . (RU) \u1051 \u1077 \u1073 \u1077 \u1076 \u1077 \u1074  \u1057 .\u1053 . (RU)"\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	97	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0authors_count\cf6 =\cf12 6\cf2 , right_holders\cf6 =\cf8 "\uc0\u1063 \u1072 \u1088 \u1089 \u1082 \u1080 \u1081  \u1042 \u1080 \u1090 \u1072 \u1083 \u1080 \u1081  \u1042 \u1083 \u1072 \u1076 \u1080 \u1084 \u1080 \u1088 \u1086 \u1074 \u1080 \u1095  (RU) \u1048 \u1074 \u1072 \u1085 \u1086 \u1074  \u1042 \u1083 \u1072 \u1076 \u1080 \u1084 \u1080 \u1088  \u1043 \u1077 \u1086 \u1088 \u1075 \u1080 \u1077 \u1074 \u1080 \u1095  (RU)"\cf2 , contact_to_third_parties\cf6 =\cf8 ""\cf2 ,program_name\cf6 =\cf8 "\uc0\u1050 \u1086 \u1084 \u1087 \u1083 \u1077 \u1082 \u1089 \u1085 \u1072 \u1103  \u1089 \u1080 \u1089 \u1090 \u1077 \u1084 \u1072  \u1080 \u1085 \u1092 \u1086 \u1088 \u1084 \u1072 \u1094 \u1080 \u1086 \u1085 \u1085 \u1086 \u1075 \u1086  \u1086 \u1073 \u1077 \u1089 \u1087 \u1077 \u1095 \u1077 \u1085 \u1080 \u1103  \u1091 \u1095 \u1077 \u1090 \u1072  \u1080  \u1076 \u1074 \u1080 \u1078 \u1077 \u1085 \u1080 \u1103  \u1082 \u1072 \u1076 \u1088 \u1086 \u1074 "\cf2 ,creation_year\cf6 =\cf2 None,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	98	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0registration_publish_date\cf6 =\cf8 "1997-06-20"\cf2 , registration_publish_number\cf6 =\cf12 2\cf2 ,actual\cf6 =\cf2 True,publication_URL\cf6 =\cf8 "http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=970019"\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	99	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	100	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf11 \kerning1\expnd0\expndtw0 {\listtext	101	}\expnd0\expndtw0\kerning0
class\cf2  AddPatentForm\cf7 (\cf2 FlaskForm\cf7 )\cf9 :\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	102	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_number \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	103	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_date \cf6 =\cf2  DateField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	104	}\expnd0\expndtw0\kerning0
\'a0 \'a0 application_number \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	105	}\expnd0\expndtw0\kerning0
\'a0 \'a0 application_date \cf6 =\cf2  DateField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	106	}\expnd0\expndtw0\kerning0
\'a0 \'a0 authors \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	107	}\expnd0\expndtw0\kerning0
\'a0 \'a0 authors_count \cf6 =\cf2  DecimalField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	108	}\expnd0\expndtw0\kerning0
\'a0 \'a0 right_holders \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	109	}\expnd0\expndtw0\kerning0
\'a0 \'a0 contact_to_third_parties \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	110	}\expnd0\expndtw0\kerning0
\'a0 \'a0 program_name \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	111	}\expnd0\expndtw0\kerning0
\'a0 \'a0 creation_year \cf6 =\cf2  DecimalField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	112	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_publish_date \cf6 =\cf2  DateField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	113	}\expnd0\expndtw0\kerning0
\'a0 \'a0 registration_publish_number \cf6 =\cf2  DecimalField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	114	}\expnd0\expndtw0\kerning0
\'a0 \'a0 actual \cf6 =\cf2  BooleanField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	115	}\expnd0\expndtw0\kerning0
\'a0 \'a0 publication_URL \cf6 =\cf2  StringField\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	116	}\expnd0\expndtw0\kerning0
\'a0 \'a0 submit \cf6 =\cf2  SubmitField\cf7 (\cf8 "Add"\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	117	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf10 \kerning1\expnd0\expndtw0 {\listtext	118	}\expnd0\expndtw0\kerning0
# Routes\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	119	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	120	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	121	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 '/'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	122	}\expnd0\expndtw0\kerning0
def main\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	123	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 return\cf2  render_template\cf7 (\cf8 'index.html'\cf2 , fields\cf6 =\cf2 fields\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	124	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	125	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	126	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 '/api/data'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	127	}\expnd0\expndtw0\kerning0
def data\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	128	}\expnd0\expndtw0\kerning0
\'a0 \'a0 query \cf6 =\cf2  Patent.\cf5 objects\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	129	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	130	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf10 # search filter\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	131	}\expnd0\expndtw0\kerning0
\'a0 \'a0 search \cf6 =\cf2  request.\cf5 args\cf2 .\cf5 get\cf7 (\cf8 'search[value]'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	132	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  search\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	133	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 query \cf6 =\cf2  query\cf7 (\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	134	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 registration_number__contains\cf6 =\cf2 search\cf7 )\cf2  \cf13 |\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	135	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 application_number__contains\cf6 =\cf2 search\cf7 )\cf2  \cf13 |\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	136	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 authors__contains\cf6 =\cf2 search\cf7 )\cf2  \cf13 |\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	137	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 right_holders__contains\cf6 =\cf2 search\cf7 )\cf2  \cf13 |\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	138	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 contact_to_third_parties__contains\cf6 =\cf2 search\cf7 )\cf2  \cf13 |\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	139	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 program_name__contains\cf6 =\cf2 search\cf7 )\cf2  \cf13 |\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	140	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 Q\cf7 (\cf2 publication_URL__contains\cf6 =\cf2 search\cf7 ))\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	141	}\expnd0\expndtw0\kerning0
\'a0 \'a0 total_filtered \cf6 =\cf2  query.\cf5 count\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	142	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	143	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf10 # response\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	144	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 return\cf2  \cf7 \{\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	145	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf8 'data'\cf9 :\cf2  \cf7 [\cf2 item.\cf5 to_dict\cf7 ()\cf2  \cf11 for\cf2  item in query\cf7 ]\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	146	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf8 'recordsTotal'\cf9 :\cf2  len\cf7 (\cf2 query\cf7 )\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	147	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf8 'recordsFiltered'\cf9 :\cf2  total_filtered,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	148	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf8 'draw'\cf9 :\cf2  request.\cf5 args\cf2 .\cf5 get\cf7 (\cf8 'draw'\cf2 , type\cf6 =\cf11 int\cf7 )\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	149	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf7 \}\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	150	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	151	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	152	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 "/adduser"\cf2 , methods\cf6 =\cf7 [\cf8 'GET'\cf2 , \cf8 'POST'\cf7 ])\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	153	}\expnd0\expndtw0\kerning0
def adduser\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	154	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  request.\cf5 method\cf2  \cf6 ==\cf2  \cf8 'GET'\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	155	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  render_template\cf7 (\cf8 "adduser.html"\cf2 , fields\cf6 =\cf2 fields\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	156	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  request.\cf5 method\cf2  \cf6 ==\cf2  \cf8 'POST'\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	157	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 username \cf6 =\cf2  request.\cf5 form\cf7 [\cf8 "username"\cf7 ]\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	158	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 password \cf6 =\cf2  request.\cf5 form\cf7 [\cf8 "password"\cf7 ]\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	159	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	160	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 User\cf7 (\cf2 username\cf6 =\cf2 username, password\cf6 =\cf2 password\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	161	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	162	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	163	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	164	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 "/addpatent"\cf2 , methods\cf6 =\cf7 [\cf8 'GET'\cf2 , \cf8 'POST'\cf7 ])\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	165	}\expnd0\expndtw0\kerning0
@login_required\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	166	}\expnd0\expndtw0\kerning0
def addpatent\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	167	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  request.\cf5 method\cf2  \cf6 ==\cf2  \cf8 'GET'\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	168	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 form \cf6 =\cf2  AddPatentForm\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	169	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  render_template\cf7 (\cf8 "addpatent.html"\cf2 , form\cf6 =\cf2 form\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	170	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  request.\cf5 method\cf2  \cf6 ==\cf2  \cf8 'POST'\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	171	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 form \cf6 =\cf2  AddPatentForm\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	172	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 Patent\cf7 (\cf2 registration_number\cf6 =\cf2 form.\cf5 registration_number\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	173	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0registration_date\cf6 =\cf2 form.\cf5 registration_date\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	174	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0application_number\cf6 =\cf2 form.\cf5 application_number\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	175	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0application_date\cf6 =\cf2 form.\cf5 application_date\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	176	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0authors\cf6 =\cf2 form.\cf5 authors\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	177	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0authors_count\cf6 =\cf2 form.\cf5 authors_count\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	178	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0right_holders\cf6 =\cf2 form.\cf5 right_holders\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	179	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0contact_to_third_parties\cf6 =\cf2 form.\cf5 contact_to_third_parties\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	180	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0program_name\cf6 =\cf2 form.\cf5 program_name\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	181	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0creation_year\cf6 =\cf2 form.\cf5 creation_year\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	182	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0registration_publish_date\cf6 =\cf2 form.\cf5 registration_publish_date\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	183	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0registration_publish_number\cf6 =\cf2 form.\cf5 registration_publish_number\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	184	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0actual\cf6 =\cf2 form.\cf5 actual\cf2 .\cf5 data\cf2 ,\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	185	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0publication_URL\cf6 =\cf2 form.\cf5 publication_URL\cf2 .\cf5 data\cf7 )\cf2 .\cf5 save\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	186	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	187	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	188	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	189	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 "/login"\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	190	}\expnd0\expndtw0\kerning0
def login\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	191	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  current_user.\cf5 is_authenticated\cf2  \cf6 ==\cf2  True\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	192	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	193	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 return\cf2  render_template\cf7 (\cf8 'login.html'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	194	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	195	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	196	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 "/login"\cf2 , methods\cf6 =\cf7 [\cf8 "POST"\cf7 ])\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	197	}\expnd0\expndtw0\kerning0
def login_post\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	198	}\expnd0\expndtw0\kerning0
\'a0 \'a0 username \cf6 =\cf2  request.\cf5 form\cf2 .\cf5 get\cf7 (\cf8 'username'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	199	}\expnd0\expndtw0\kerning0
\'a0 \'a0 password \cf6 =\cf2  request.\cf5 form\cf2 .\cf5 get\cf7 (\cf8 'password'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	200	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	201	}\expnd0\expndtw0\kerning0
\'a0 \'a0 user \cf6 =\cf2  User.\cf5 objects\cf7 (\cf2 username\cf6 =\cf2 username\cf7 )\cf2 .\cf5 first\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	202	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf10 #users.find_one(\{"username" : username\})\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	203	}\expnd0\expndtw0\kerning0
\'a0 \'a0 print\cf7 (\cf2 user\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	204	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  not user\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	205	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 flash\cf7 (\cf8 '\uc0\u1058 \u1072 \u1082 \u1086 \u1075 \u1086  \u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1103  \u1085 \u1077  \u1089 \u1091 \u1097 \u1077 \u1089 \u1090 \u1074 \u1091 \u1077 \u1090 !'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	206	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/login'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	207	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 if\cf2  user\cf7 [\cf8 'password'\cf7 ]\cf2  \cf13 !\cf6 =\cf2  password\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	208	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 flash\cf7 (\cf8 '\uc0\u1053 \u1077 \u1087 \u1088 \u1072 \u1074 \u1080 \u1083 \u1100 \u1085 \u1099 \u1081  \u1087 \u1072 \u1088 \u1086 \u1083 \u1100 !'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	209	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/login'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	210	}\expnd0\expndtw0\kerning0
\'a0 \'a0 login_user\cf7 (\cf2 user\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	211	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	212	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	213	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	214	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	215	}\expnd0\expndtw0\kerning0
@app.\cf5 route\cf7 (\cf8 "/logout"\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	216	}\expnd0\expndtw0\kerning0
@login_required\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	217	}\expnd0\expndtw0\kerning0
def logout\cf7 ()\cf9 :\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	218	}\expnd0\expndtw0\kerning0
\'a0 \'a0 logout_user\cf7 ()\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	219	}\expnd0\expndtw0\kerning0
\'a0 \'a0 \cf11 return\cf2  redirect\cf7 (\cf8 '/'\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	220	}\expnd0\expndtw0\kerning0
\'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	221	}\expnd0\expndtw0\kerning0
\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf11 \kerning1\expnd0\expndtw0 {\listtext	222	}\expnd0\expndtw0\kerning0
if\cf7 (\cf2 __name__ \cf6 ==\cf2  \cf8 "__main__"\cf7 )\cf9 :\cf2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	223	}\expnd0\expndtw0\kerning0
\'a0 \'a0 app.\cf5 run\cf7 (\cf2 host\cf6 =\cf8 '0.0.0.0'\cf2 , port\cf6 =\cf12 5001\cf7 )\cf2 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	224	}\expnd0\expndtw0\kerning0
\'a0}
PGDMP                         w            portfolio_site    11.1    11.1 �    !           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            "           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            #           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            $           1262    16891    portfolio_site    DATABASE     �   CREATE DATABASE portfolio_site WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE portfolio_site;
             danieln    false            %           0    0    DATABASE portfolio_site    ACL     3   GRANT ALL ON DATABASE portfolio_site TO portfolio;
                  danieln    false    3364            �            1259    16923 
   auth_group    TABLE     e   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public      	   portfolio    false            �            1259    16921    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public    	   portfolio    false    203            &           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public    	   portfolio    false    202            �            1259    16933    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public      	   portfolio    false            �            1259    16931    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public    	   portfolio    false    205            '           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public    	   portfolio    false    204            �            1259    16915    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public      	   portfolio    false            �            1259    16913    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public    	   portfolio    false    201            (           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public    	   portfolio    false    200            �            1259    16941 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public      	   portfolio    false            �            1259    16951    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public      	   portfolio    false            �            1259    16949    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public    	   portfolio    false    209            )           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
            public    	   portfolio    false    208            �            1259    16939    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public    	   portfolio    false    207            *           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
            public    	   portfolio    false    206            �            1259    16959    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public      	   portfolio    false            �            1259    16957 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public    	   portfolio    false    211            +           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
            public    	   portfolio    false    210            �            1259    17019    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public      	   portfolio    false            �            1259    17017    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public    	   portfolio    false    213            ,           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public    	   portfolio    false    212            �            1259    16905    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public      	   portfolio    false            �            1259    16903    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public    	   portfolio    false    199            -           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public    	   portfolio    false    198            �            1259    16894    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public      	   portfolio    false            �            1259    16892    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public    	   portfolio    false    197            .           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public    	   portfolio    false    196            �            1259    17102    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public      	   portfolio    false            �            1259    17047    portfolio_app_blog    TABLE     �   CREATE TABLE public.portfolio_app_blog (
    id uuid NOT NULL,
    title character varying(200) NOT NULL,
    content text NOT NULL,
    pub_date timestamp with time zone NOT NULL,
    slug character varying(50),
    category_id uuid
);
 &   DROP TABLE public.portfolio_app_blog;
       public      	   portfolio    false            �            1259    17073    portfolio_app_blog_tags    TABLE     ~   CREATE TABLE public.portfolio_app_blog_tags (
    id integer NOT NULL,
    blog_id uuid NOT NULL,
    tag_id uuid NOT NULL
);
 +   DROP TABLE public.portfolio_app_blog_tags;
       public      	   portfolio    false            �            1259    17071    portfolio_app_blog_tags_id_seq    SEQUENCE     �   CREATE SEQUENCE public.portfolio_app_blog_tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.portfolio_app_blog_tags_id_seq;
       public    	   portfolio    false    218            /           0    0    portfolio_app_blog_tags_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.portfolio_app_blog_tags_id_seq OWNED BY public.portfolio_app_blog_tags.id;
            public    	   portfolio    false    217            �            1259    17113    portfolio_app_blogcomment    TABLE     �   CREATE TABLE public.portfolio_app_blogcomment (
    id uuid NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    content text NOT NULL,
    parent_id uuid NOT NULL
);
 -   DROP TABLE public.portfolio_app_blogcomment;
       public      	   portfolio    false            �            1259    17055    portfolio_app_category    TABLE     �   CREATE TABLE public.portfolio_app_category (
    id uuid NOT NULL,
    title character varying(100) NOT NULL,
    slug character varying(50)
);
 *   DROP TABLE public.portfolio_app_category;
       public      	   portfolio    false            �            1259    17062    portfolio_app_tag    TABLE     �   CREATE TABLE public.portfolio_app_tag (
    id uuid NOT NULL,
    title character varying(100) NOT NULL,
    slug character varying(50)
);
 %   DROP TABLE public.portfolio_app_tag;
       public      	   portfolio    false            0           2604    16926    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    203    202    203            1           2604    16936    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    204    205    205            /           2604    16918    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    201    200    201            2           2604    16944    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    207    206    207            3           2604    16954    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    209    208    209            4           2604    16962    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    211    210    211            5           2604    17022    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    212    213    213            .           2604    16908    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    198    199    199            -           2604    16897    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    197    196    197            7           2604    17076    portfolio_app_blog_tags id    DEFAULT     �   ALTER TABLE ONLY public.portfolio_app_blog_tags ALTER COLUMN id SET DEFAULT nextval('public.portfolio_app_blog_tags_id_seq'::regclass);
 I   ALTER TABLE public.portfolio_app_blog_tags ALTER COLUMN id DROP DEFAULT;
       public    	   portfolio    false    218    217    218                      0    16923 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public    	   portfolio    false    203   W�                 0    16933    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public    	   portfolio    false    205   t�                 0    16915    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public    	   portfolio    false    201   ��                 0    16941 	   auth_user 
   TABLE DATA               �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public    	   portfolio    false    207   6�                 0    16951    auth_user_groups 
   TABLE DATA               A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public    	   portfolio    false    209   �                 0    16959    auth_user_user_permissions 
   TABLE DATA               P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public    	   portfolio    false    211   �                 0    17019    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public    	   portfolio    false    213   �       	          0    16905    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public    	   portfolio    false    199   |�                 0    16894    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public    	   portfolio    false    197   
�                 0    17102    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public    	   portfolio    false    219   Ź                 0    17047    portfolio_app_blog 
   TABLE DATA               ]   COPY public.portfolio_app_blog (id, title, content, pub_date, slug, category_id) FROM stdin;
    public    	   portfolio    false    214   �                 0    17073    portfolio_app_blog_tags 
   TABLE DATA               F   COPY public.portfolio_app_blog_tags (id, blog_id, tag_id) FROM stdin;
    public    	   portfolio    false    218   ��                 0    17113    portfolio_app_blogcomment 
   TABLE DATA               X   COPY public.portfolio_app_blogcomment (id, name, email, content, parent_id) FROM stdin;
    public    	   portfolio    false    220   ]�                 0    17055    portfolio_app_category 
   TABLE DATA               A   COPY public.portfolio_app_category (id, title, slug) FROM stdin;
    public    	   portfolio    false    215   z�                 0    17062    portfolio_app_tag 
   TABLE DATA               <   COPY public.portfolio_app_tag (id, title, slug) FROM stdin;
    public    	   portfolio    false    216   �       0           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
            public    	   portfolio    false    202            1           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
            public    	   portfolio    false    204            2           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);
            public    	   portfolio    false    200            3           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
            public    	   portfolio    false    208            4           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);
            public    	   portfolio    false    206            5           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
            public    	   portfolio    false    210            6           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 13, true);
            public    	   portfolio    false    212            7           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);
            public    	   portfolio    false    198            8           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);
            public    	   portfolio    false    196            9           0    0    portfolio_app_blog_tags_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.portfolio_app_blog_tags_id_seq', 6, true);
            public    	   portfolio    false    217            E           2606    16930    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public      	   portfolio    false    203            J           2606    16985 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public      	   portfolio    false    205    205            M           2606    16938 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public      	   portfolio    false    205            G           2606    16928    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public      	   portfolio    false    203            @           2606    16971 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public      	   portfolio    false    201    201            B           2606    16920 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public      	   portfolio    false    201            U           2606    16956 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public      	   portfolio    false    209            X           2606    17000 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public      	   portfolio    false    209    209            O           2606    16946    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public      	   portfolio    false    207            [           2606    16964 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public      	   portfolio    false    211            ^           2606    17014 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public      	   portfolio    false    211    211            R           2606    17042     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public      	   portfolio    false    207            a           2606    17028 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public      	   portfolio    false    213            ;           2606    16912 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public      	   portfolio    false    199    199            =           2606    16910 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public      	   portfolio    false    199            9           2606    16902 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public      	   portfolio    false    197            {           2606    17109 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public      	   portfolio    false    219            e           2606    17054 *   portfolio_app_blog portfolio_app_blog_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.portfolio_app_blog
    ADD CONSTRAINT portfolio_app_blog_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.portfolio_app_blog DROP CONSTRAINT portfolio_app_blog_pkey;
       public      	   portfolio    false    214            h           2606    17070 .   portfolio_app_blog portfolio_app_blog_slug_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.portfolio_app_blog
    ADD CONSTRAINT portfolio_app_blog_slug_key UNIQUE (slug);
 X   ALTER TABLE ONLY public.portfolio_app_blog DROP CONSTRAINT portfolio_app_blog_slug_key;
       public      	   portfolio    false    214            u           2606    17099 L   portfolio_app_blog_tags portfolio_app_blog_tags_blog_id_tag_id_884d86ec_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.portfolio_app_blog_tags
    ADD CONSTRAINT portfolio_app_blog_tags_blog_id_tag_id_884d86ec_uniq UNIQUE (blog_id, tag_id);
 v   ALTER TABLE ONLY public.portfolio_app_blog_tags DROP CONSTRAINT portfolio_app_blog_tags_blog_id_tag_id_884d86ec_uniq;
       public      	   portfolio    false    218    218            w           2606    17078 4   portfolio_app_blog_tags portfolio_app_blog_tags_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.portfolio_app_blog_tags
    ADD CONSTRAINT portfolio_app_blog_tags_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.portfolio_app_blog_tags DROP CONSTRAINT portfolio_app_blog_tags_pkey;
       public      	   portfolio    false    218                       2606    17120 8   portfolio_app_blogcomment portfolio_app_blogcomment_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.portfolio_app_blogcomment
    ADD CONSTRAINT portfolio_app_blogcomment_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.portfolio_app_blogcomment DROP CONSTRAINT portfolio_app_blogcomment_pkey;
       public      	   portfolio    false    220            j           2606    17059 2   portfolio_app_category portfolio_app_category_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.portfolio_app_category
    ADD CONSTRAINT portfolio_app_category_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.portfolio_app_category DROP CONSTRAINT portfolio_app_category_pkey;
       public      	   portfolio    false    215            m           2606    17061 6   portfolio_app_category portfolio_app_category_slug_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.portfolio_app_category
    ADD CONSTRAINT portfolio_app_category_slug_key UNIQUE (slug);
 `   ALTER TABLE ONLY public.portfolio_app_category DROP CONSTRAINT portfolio_app_category_slug_key;
       public      	   portfolio    false    215            o           2606    17066 (   portfolio_app_tag portfolio_app_tag_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.portfolio_app_tag
    ADD CONSTRAINT portfolio_app_tag_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.portfolio_app_tag DROP CONSTRAINT portfolio_app_tag_pkey;
       public      	   portfolio    false    216            r           2606    17068 ,   portfolio_app_tag portfolio_app_tag_slug_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.portfolio_app_tag
    ADD CONSTRAINT portfolio_app_tag_slug_key UNIQUE (slug);
 V   ALTER TABLE ONLY public.portfolio_app_tag DROP CONSTRAINT portfolio_app_tag_slug_key;
       public      	   portfolio    false    216            C           1259    16973    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public      	   portfolio    false    203            H           1259    16986 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public      	   portfolio    false    205            K           1259    16987 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public      	   portfolio    false    205            >           1259    16972 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public      	   portfolio    false    201            S           1259    17002 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public      	   portfolio    false    209            V           1259    17001 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public      	   portfolio    false    209            Y           1259    17016 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public      	   portfolio    false    211            \           1259    17015 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public      	   portfolio    false    211            P           1259    17043     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public      	   portfolio    false    207            _           1259    17039 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public      	   portfolio    false    213            b           1259    17040 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public      	   portfolio    false    213            y           1259    17111 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public      	   portfolio    false    219            |           1259    17110 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public      	   portfolio    false    219            c           1259    17082 '   portfolio_app_blog_category_id_299fa1d6    INDEX     m   CREATE INDEX portfolio_app_blog_category_id_299fa1d6 ON public.portfolio_app_blog USING btree (category_id);
 ;   DROP INDEX public.portfolio_app_blog_category_id_299fa1d6;
       public      	   portfolio    false    214            f           1259    17081 %   portfolio_app_blog_slug_0861d41e_like    INDEX     x   CREATE INDEX portfolio_app_blog_slug_0861d41e_like ON public.portfolio_app_blog USING btree (slug varchar_pattern_ops);
 9   DROP INDEX public.portfolio_app_blog_slug_0861d41e_like;
       public      	   portfolio    false    214            s           1259    17100 (   portfolio_app_blog_tags_blog_id_d0e6d8aa    INDEX     o   CREATE INDEX portfolio_app_blog_tags_blog_id_d0e6d8aa ON public.portfolio_app_blog_tags USING btree (blog_id);
 <   DROP INDEX public.portfolio_app_blog_tags_blog_id_d0e6d8aa;
       public      	   portfolio    false    218            x           1259    17101 '   portfolio_app_blog_tags_tag_id_9ea64c70    INDEX     m   CREATE INDEX portfolio_app_blog_tags_tag_id_9ea64c70 ON public.portfolio_app_blog_tags USING btree (tag_id);
 ;   DROP INDEX public.portfolio_app_blog_tags_tag_id_9ea64c70;
       public      	   portfolio    false    218            }           1259    17126 ,   portfolio_app_blogcomment_parent_id_19867f22    INDEX     w   CREATE INDEX portfolio_app_blogcomment_parent_id_19867f22 ON public.portfolio_app_blogcomment USING btree (parent_id);
 @   DROP INDEX public.portfolio_app_blogcomment_parent_id_19867f22;
       public      	   portfolio    false    220            k           1259    17079 )   portfolio_app_category_slug_be229008_like    INDEX     �   CREATE INDEX portfolio_app_category_slug_be229008_like ON public.portfolio_app_category USING btree (slug varchar_pattern_ops);
 =   DROP INDEX public.portfolio_app_category_slug_be229008_like;
       public      	   portfolio    false    215            p           1259    17080 $   portfolio_app_tag_slug_0eb6cca9_like    INDEX     v   CREATE INDEX portfolio_app_tag_slug_0eb6cca9_like ON public.portfolio_app_tag USING btree (slug varchar_pattern_ops);
 8   DROP INDEX public.portfolio_app_tag_slug_0eb6cca9_like;
       public      	   portfolio    false    216            �           2606    16979 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public    	   portfolio    false    201    205    3138            �           2606    16974 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public    	   portfolio    false    203    205    3143            �           2606    16965 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public    	   portfolio    false    3133    201    199            �           2606    16994 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public    	   portfolio    false    3143    203    209            �           2606    16989 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public    	   portfolio    false    3151    209    207            �           2606    17008 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public    	   portfolio    false    211    3138    201            �           2606    17003 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public    	   portfolio    false    207    211    3151            �           2606    17029 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public    	   portfolio    false    199    3133    213            �           2606    17034 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public    	   portfolio    false    3151    207    213            �           2606    17083 G   portfolio_app_blog portfolio_app_blog_category_id_299fa1d6_fk_portfolio    FK CONSTRAINT     �   ALTER TABLE ONLY public.portfolio_app_blog
    ADD CONSTRAINT portfolio_app_blog_category_id_299fa1d6_fk_portfolio FOREIGN KEY (category_id) REFERENCES public.portfolio_app_category(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.portfolio_app_blog DROP CONSTRAINT portfolio_app_blog_category_id_299fa1d6_fk_portfolio;
       public    	   portfolio    false    215    214    3178            �           2606    17088 J   portfolio_app_blog_tags portfolio_app_blog_t_blog_id_d0e6d8aa_fk_portfolio    FK CONSTRAINT     �   ALTER TABLE ONLY public.portfolio_app_blog_tags
    ADD CONSTRAINT portfolio_app_blog_t_blog_id_d0e6d8aa_fk_portfolio FOREIGN KEY (blog_id) REFERENCES public.portfolio_app_blog(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.portfolio_app_blog_tags DROP CONSTRAINT portfolio_app_blog_t_blog_id_d0e6d8aa_fk_portfolio;
       public    	   portfolio    false    218    3173    214            �           2606    17093 W   portfolio_app_blog_tags portfolio_app_blog_tags_tag_id_9ea64c70_fk_portfolio_app_tag_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.portfolio_app_blog_tags
    ADD CONSTRAINT portfolio_app_blog_tags_tag_id_9ea64c70_fk_portfolio_app_tag_id FOREIGN KEY (tag_id) REFERENCES public.portfolio_app_tag(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.portfolio_app_blog_tags DROP CONSTRAINT portfolio_app_blog_tags_tag_id_9ea64c70_fk_portfolio_app_tag_id;
       public    	   portfolio    false    3183    218    216            �           2606    17121 N   portfolio_app_blogcomment portfolio_app_blogco_parent_id_19867f22_fk_portfolio    FK CONSTRAINT     �   ALTER TABLE ONLY public.portfolio_app_blogcomment
    ADD CONSTRAINT portfolio_app_blogco_parent_id_19867f22_fk_portfolio FOREIGN KEY (parent_id) REFERENCES public.portfolio_app_blogcomment(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.portfolio_app_blogcomment DROP CONSTRAINT portfolio_app_blogco_parent_id_19867f22_fk_portfolio;
       public    	   portfolio    false    3199    220    220                  x������ � �            x������ � �         �  x�]��n�0E����h���F�����BtS�~�vb��$� ��>�����>E�������x�+��\~�q��'+��Vғ�5����g��A�c6{��q[��4���NZ΀l��F��ۊ�!�Qq]����t
��A˥����)!��H)*	@��l�Z��j؎�k=�SO�QOg��p���h
�<�2�k�Z����р�����,d�N{�x��|y������z	��
�J�wa�3c�킱^�T�B��Hӿc�]�:�JSoNY� �iX� Ud�q8���K��a��aK��+T�ÊJkˠi�Ӿ2���0ZT���k?���	*�i�Xc�h�Y c�g
q,F��B���;��O���OP���hZ�'����?P�J��5���%�� ����         �   x�e��
�0@��+�Ic�ikA-��Hu�i��Ї5����8@e���G�2� ���6���H���'t��Ͷ6E�[����ZMԹ��A��&E�us�f>G�B�e,y�ƜK2]>+B��g�X^������e(�I/�R�*�.`            x������ � �            x������ � �         N  x�͔�n1���S�<p����ʼBJ�m'�d����=+	Hl��	��ؙo�C��,Dc���v0Y?Q	��|�vH��3y�1�!���^�B+�B��t3�p��I������//�C`��x]Dw0���l��h��M���+p�����܁'����wRB��`N��X��Fnȥ'ta����8?m?25�L��Bt�SDͫj.Lj⻉%8#�[��)�_����>�he^�d��4Ai�_YC� LFp p��|�p����P0R
��m,��4�L,���S?Z"8���T.�.�z�1#R�Ч����׼���^ܨ%A������0Ħ)f#!wMBj5{�o�^2�V��8)R����K+&���]�ɱi��8����\2�D�iD�0Z/O��T:p1�����+hp*M�C�����L,р}���<�d���dU�%,�U�kR��y(-kM�C����:���LhG
z*C�d���z��y}�]��|o-ɐ���ewf@��`����u�r�v7'�M�k����W����m7o��,�՛�`��O�#�&���q�Z�<o��      	   ~   x�mNI
1<w=Fw�"H&�10I7I�0�782x��Zr�3M8[��#��E�%�Z�d�%i��BZ�#y��c6+�_�U����L*Ş2E�;U�$.+�;� ��ue��*���Wq� x ;G�         �  x����n� F������3Ïɳ��؄�Hظ�T۷_�Y�R\%7���x|f���ݘ����1Ə>{:d�_��zA80~|��/�v��K~�@�$�Ξ?>�u��[M��Rh�2��ә��h���P��2čA7F�{�>��-س9�G,6YZ��%�t��j��ޘ�nE��dE���Kfri��\K�y3ؿ&��\��D!�VT���J���p���!�H�F�+��ԣU��m�8��``+C|g;�jޗ��힓 �V�,n?.>�r�uS��� &�Anө��|��O6�4�޻�b2��g{���$��:Њ�7�<��.�������P�dj%�)���/k0M���4gj)C�gqY�d� 0��pԌ/�U7�6�O�:8I��FB�v2ʄ�0�>�yd/%���^�d˨���v��FM�           x�=�Mo�0 @��W���Cp�찉���(m�.ö����s;,y���w��Kw�������=����:ޥzO�m�{pב@t���6�9�$h���z9M��
�"�����Ƀ�_V|s�8�9��=K�Z���^q�*�uũ)���ל��'�GgY��}��{q܌{Fn�g`�p��rti�6�X�R��m�V����B�(9��D��'��������qK)J�C@Y:$m�
��y$z�,9��'��
��g���c<�A f� �k�8��=gU         �  x��Z�n�6}����׊�3�8����(ҧ ER3L�E$�N����2N� 
�I�ǖ%�.�{e�L���/2�yMK~H�Σ"-�e�g�| F�FmF՝��/�f���/�%Q\�(��$�)*NQ�C�]���<9�8M+V��1����,dZ����<�],yV��8�G�3Z�qq�����b@���l��m��~$Z�Zi��NKn��#aBJs�"�Q&$�/L˦��t�a�R����qn[�:�:#G�W����Z����-�Q�m�d�6��Շ�w�U�%�0b�_��ʋ�aX`���~�t�2 -{T-�_�a+Wp�k�X30x�����숈j�U�4��#�
��Vv;m���:$8OW6*�.3�+� q�CD�-;#5"���l�� :��=��.�A�!��MK���v�F~�z*�[����)�:���}��W�����%F��c����g�ܰ�!����rPv|�M����lX�X�v|۹��z�UG�^[9"{�\U�Ʃ��oCø��c��G��C@s��rq�:[�_:��J�X��� ��,`kP��c�T�`�
3vD��O��*4a�,�o���x�pWp�ұ���2�q&�0���D�,���4l,7&�H�B�m�1��|N^�v� �T-;��5	s���-�|����oibp.���pkdӚ����z�[+�蟠���*1O�'%\:��
�y�~�\����z:n �1/m��K�̂	>�V�ھ�Y����s��Q�:U���ͷ[8��]��j�/#�M(�#�/��a0��5e�b4}��K0�֯f�E��k��]7���D$]롩�f���f��\��a�P����D�5�Wn�N6e�YLT�%5=�sD_�#፝�m�����[d����N�nk��`����ɂ�*X�Z�q�����H��x�#ĕ����2w��c5D|N�Z����)��|���G3��ů��ӆ�U]��������Z6��F�~Ā̘E~l�	���X�<�g�͒��8'qy��S�|I�i�m���uͳ��i*4ceE���� +�4U�y�P���&���ob���&���?��h\:�O��\���1�֏����Ի�

�Ni~`ձ���4gw\����B�EE�R�0�fE,�I*�d��M�7��$~��M�7����qB�x��$y*�x��&�/��q�i̢#�ʢ�{<^�3.!�)���L��A�M�7������|0m>6����GC����ĥ+�n%սj�hz�b�#z�/vc}��?�������'&�����"ڿ��	)�/������wQ�.J�
��(����y�x�Hu�tK9<>'J��)���qG�/��v^��+�ye;�l���'���ˁ;�Oq��y%���������_Q�ѳ         �   x����� !Dѳ�[2@+��E@�a�����7�*)J
;�9^��:�M�ζ�@��R����sR�wzq=�7k�~rG�q�p�P��Y�b�Gڲ��Ϙ�H��f��1�{�o�6��$���9�\Z=�+L���e�߆��\���7����|���օv?���īORǝ�����6v����y��Y�q9            x������ � �         ~   x�E�1�0 ��/F%���,��H�JE���SXXNw�Qo��ud9��q�rT��kii���_�5���Q��zk��jj݄i�z�<��+�_frA�aC	����#͈.ɶ��C��r��,�         y   x�5�1� F�9��+��ܥ6�vHՁ%�o������
�DʌZ�)ggݥ���]�v��=.I5̈�l���"��h��肱�����!1��qtLN�����ŇiGi����K�߈��+c     
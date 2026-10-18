# 第八章　已有工具、具体结论与两个保留附录

本章对应原稿§8（基线第16—17页）和附录A、B（第17—18页）。这一部分有两种任务：说明本文结论与已有理论的实际接口；把正文使用的共同坐标和一个特定版本文献说明展开。它不是重新进行无边界文献审查，也不把“没有在已读文献找到完全相同表述”当作原创性证明。

## 8.1 哪些工具已经存在，本文究竟把什么合成起来

可以将已读文献的作用按证明位置理解。

|来源及已核位置|在本稿中的实际作用|不能由它直接声称的结论|
|---|---|---|
|Kaur–Kulshrestha，arXiv:1210.3790v1，Lemma 2.4，PDF第6—7页|正交和与沿共同中心的中心积对应|不是本稿四元子群极值分类|
|Kaur–Kulshrestha，arXiv:1510.06583v1，Proposition 3.5、Remark 3.6，第8页|此群类的不可约字符及三个非线性字符的来源|没有以此自动核读Zahinda原文的全部分类|
|Abdukhalikov–Feng–Ho（AFH），Theorem 2.1，印刷pp.509—510|实际二元标量Walsh对偶；允许二元线性细化|不是三个分量的共同严格等价分类|
|AFH，p.509及Theorem 2.2，pp.511—512|已满足较大基域齐次性后的型别、相位及正余块解释|不能因使用四元域坐标便将核心当作四元域齐次型|
|Çeşmelioğlu–Meidl–Pott（CMP），式(4)，p.313|一般Maiorana–McFarland对偶公式，含任意额外函数及原点相位|不是不经联立等号条件便自动得到96个筛选|
|CMP，Theorem 2(i)，p.314|标准迹乘积正端构造，须保留子域线性及相应假设|不把任意二元线性置换误作四元域线性置换|
|Wang–Fu–Wei（WFW），arXiv:2301.00581v1，Theorem 6，式(35)，pp.23—24|$D\equiv0$ 上端的部分差集参数|不直接覆盖非半单下端|
|交替矩阵笔及局部等价理论，LM、PFMR、MPG的指定版本和位置|成对循环块、局部环输入变换的框架|同族不等于群同构；不能丢弃完整线性细化|

AFH与CMP的全文已实际取得并完成项目中的命题级比较，不是当前取文缺口。它们不是“只与关键词有关”的背景文献：正文第五、六章的实际相位正是旧公式的代入；给定等号极化后，96个筛选及核心—整个余块的补偿排除，都是旧公式加经典各向异性判据的短推导。本稿不把这些步骤包装成新的通用对偶理论、规范形算法或新方法。

当前具体合成结论是：先由群计数得到三阶Walsh矩；利用交替笔的维数亏损求出最优数值界及全部等号条件；在偶数 $n\ge4$ 下联立完整细化条件，再以同一目标固定归一，得到整个下端群的唯一同构类型。已经核读的上述定理未直接代替整条结论，这不意味着其他文献不可能已有同一特例。历史位置与数学证明的有效性是两个问题，不能混写。

Zahinda关于totally orthogonal特殊2群的完整细化分类是否已经覆盖中心 $C_2^2$ 的有关结构，仍是具体历史问题；本文使用其Arf判据的引用链已经明确，未据此声称核读该原文所有结果。CMP2021、Fitzgerald–Yucas、Bornand及后续结构论文也仅保留真实未核的具体范围，不把每个未读书目自动改写为本稿数学证明缺口。细节留在项目文献记录，不需要塞进数学证明正文。

## 8.2 最大自逆数分支与totally orthogonal的准确联系

这段在正文§8中给出另一种文献入口，并不承担最优界的自足证明。不熟悉表示论的读者可先理解结论：这里“最大自逆元素数”恰是这个群类的“所有不可约字符Frobenius–Schur指标均为正”分支。它使Zahinda文献与本问题有真实联系，而非只因标题相似。

简要补充必要记号。一个复表示把群元映成可逆复矩阵，其字符 $\chi(g)$ 为矩阵迹。不可约表示是不能分成更小不变子空间直和的表示。Frobenius–Schur指标定义为

$$
\nu(\chi)=\frac1{|G|}\sum_{g\in G}\chi(g^2).
$$

经典判据说明：不可约字符的指标为 $+1$ 时可由实正交表示实现；所有不可约字符都满足这一性质便称totally orthogonal。这个表示论判据是已有背景，不在本文重新证明。

在本群类中，$G/G'=V$ 是阶 $N$ 的二元初等阿贝尔群，所以有 $N$ 个线性字符，它们只取 $\pm1$，且 $\chi(g^2)=1$，指标均为1。按KK15 Proposition 3.5、Remark 3.6，还有三个度为 $h=2^n$ 的不可约字符 $\chi_\lambda$，分别来自三个extraspecial商。其限制到中心为

$$
\chi_\lambda(w)=h(-1)^{\lambda(w)},\qquad
\lambda\in W^*\setminus\{0\}.
$$

这已经列完所有不可约字符：它们的度数平方和为 $N+3h^2=4N=|G|$。因为每个 $g^2\in W$，且每个 $v\in V$ 有四个提升，指标变为

$$
\begin{aligned}
\nu(\chi_\lambda)
&=\frac1{4N}\sum_g h(-1)^{\lambda(g^2)}\\
&=\frac{4h}{4N}\sum_{v\in V}(-1)^{\lambda Q(v)}
=\frac{\mathcal G(\lambda Q)}h.
\end{aligned}
$$

所以这三个指标全为1，当且仅当三个原始Gauss和全为 $+h$，也就当且仅当 $s=N+3h$。KK12 Theorem 4.1、第12页重述了相应Arf判据，并将其归于Zahinda Theorem 3.5；这里准确地通过KK使用这条归属，没有将间接引用升级为已检查Zahinda全部原文。

## 8.3 三个对偶的闭合：$D\equiv0$的真正含义

设三个原分量为 $q_1,q_2,q_3=q_1+q_2$。实际Walsh对偶由

$$
\mathcal W_{q_i}(\xi)=h(-1)^{q_i^*(\xi)}
$$

唯一决定，包括原点相位。在最大 $s$ 分支上三者的原点相位都为0。三个对偶均为非零且互异的函数：每个对偶仍bent，零函数不是正维bent；若两个对偶相同，两个Walsh变换相同，由Fourier反演原分量相同，这将使第三标量分量为零，与极化非退化矛盾。

CMP Definition 1、p.309中的vectorial dual-bent，要求非零分量的实际对偶加零函数构成相同输出维数的函数向量空间。本题输出维数是2，非零元素只有三个，故这个要求恰为

$$
\{0,q_1^*,q_2^*,q_3^*\}\text{对加法封闭}
\quad\Longleftrightarrow\quad q_1^*+q_2^*=q_3^*
\quad\Longleftrightarrow\quad D\equiv0.
$$

在一般输出维数中，向量对偶的标签选择要另外处理；此处三个非零标签的任意重排都来自 $\operatorname{GL}_2(\mathbb F_2)$，因为该群有6个元素并忠实作用为三个非零向量的所有置换。因此不能把一般维数的复杂标签问题，照搬成本题尚未解决的障碍。

有一条很容易误用的矩阵恒等式：

$$
B_1^{-1}+B_2^{-1}
=B_1^{-1}(B_1+B_2)B_2^{-1}.
$$

右边三个因子均可逆，所以左边可逆。这意味着任意两个对偶之和仍是非退化二元二次函数，因而bent。但它没有说明这个和就是第三个对偶；后者还要求完整二次细化相同，恰是 $D\equiv0$。由“每两个对偶的和bent”跳到“对偶闭合”，遗漏了核心问题。

还必须区分三件事：$D\equiv0$ 是完整函数恒零；$C=0$ 是 $D$ 的极化恒零，只能推出 $D$ 为线性函数（在整体规范 $D(0)=0$ 下）；$\mathcal G(D)=0$ 是整数字符和相消，可能来自非零线性根限制。若 $D\equiv0$，反而 $\mathcal G(D)=N$，不是0。

## 8.4 为什么$D\equiv0$上端明确属于旧定理的直接推论

这一步不是笼统地说“与部分差集有关”，而是原稿§8已经实际完成的参数代入。最大 $s$ 加 $D\equiv0$ 提供同标签向量对偶，满足WFW Theorem 6的Condition A。取其参数为 $p=2$、输入维数 $2n$、输出维数2、regular系数 $\epsilon=1$、$F=Q$、$F(0)=0$，并取值集 $I=\{0\}$。输出维数条件 $2\le n$ 在本题有效维数内成立。

旧定理给 $E=Q^{-1}(0)\setminus\{0\}$ 为部分差集。需要用到的参数为

$$
z=\frac{N+3h}{4},\quad k=|E|=z-1,
\quad\lambda=\frac N{16}+\frac{3h}{4}-2.
$$

部分差集参数 $\lambda$ 的含义是：对每个固定 $x\in E$，有 $\lambda$ 个有序对 $(y,z')\in E^2$ 使 $y-z'=x$。二元加法中减号与加号相同，因此这些恰是 $x,y,x+y$ 全在非零零点集中的计数。总计 $k\lambda$ 个有序基，每个全零二维子空间有6个有序基，所以 $6L=k\lambda$。再用引理2.3的提升公式，

$$
v_4=16L+6z-5=\frac83 k\lambda+6z-5.
$$

为了看清与 $M_n$ 的关系，写 $N=h^2$，代入可得

$$
\begin{aligned}
v_4
&=\frac{(h^2+3h-4)(h^2+12h-32)}{24}
+\frac{36h^2+108h-120}{24}\\
&=\frac{h^4+15h^3+36h^2-36h+8}{24}
=M_n+\frac{h^3}{4}.
\end{aligned}
$$

即 $M_n+2^{3n-2}$。这是明确的旧定理直接推论，应在贡献叙述中承认。它不同时给出非 $D\equiv0$ 的下端，也不能将“regular”误当每个正交限制块的零频和为正。

## 8.5 EA等价与completed class为什么不能代替群同构

本稿严格等价要求 $Q'(Sx)=TQ(x)$，其中 $S,T$ 同时作用于完整映射，且二元线性可逆。CMP的extended affine（EA）等价更宽，允许

$$
\widetilde Q(x)=TQ(Sx+a)+Lx+b.
$$

输入平移 $a$、任意线性添加 $L$ 及目标常数 $b$ 不属于本稿群同构关系。它们也可能改变零点计数和实际对偶闭合。比如 $uv$ 与 $uv+u$ 仅差一次项，却分别有69和53个四元子群；第五章的基准核心与 $Q_*$ 也同属一个EA类，却给不同的 $v_4$。

不过，不能仅以“下端对象自身不闭合”便排除全部EA路径，因为EA确实会改变闭合性。正确的不变量是极化秩：在上述全部EA操作下，三个极化满足

$$
\widetilde B_\lambda=S^{\mathsf T}B_{T^*\lambda}S.
$$

平移、添加线性项和常数不改变二次极化；目标 $T$ 只置换三个非零标签。因此三逆极化和变为

$$
\widetilde C=S^{-1}CS^{-\mathsf T}.
$$

所以 $\operatorname{rank}C$ 在完整EA范围内保持。下端 $\operatorname{rank}C=4$，而二次对偶闭合源有 $C=0$，故下端不能整体EA等价于这样的闭合源。这一论证针对完整EA范围，而非只证明严格等价不变量后越界使用。

CMP Theorem 1、p.311的前提是存在向量对偶，其结论是completed class中的**标量函数集合**取对偶后的关系。它允许分别找到三个标量的实现，不会保证它们由同一个输入变换、同一个线性添加和同一个目标操作同时实现。各标量分别可化到标准二次型，是比完整向量映射共同分类弱得多的信息。上述秩论证排除了共同闭合源的EA代表，并没有否认每个标量分别属于某个completed class。

LM Theorem 1.2计数的是同族类，而非本稿完整平方映射同构类；其另外一些分解定理还带指数 $p$ 假设，本题指数为4，不能未经核对套用。PFMR在特征2的局部理论则确实保留对角平方所表示的二元线性项，因此不能以“齐次二次型”四字排除其覆盖。稿件保留显式换基，使证明不依赖一条未经检查的宽泛算法声明。

## 8.6 附录A：为什么三个核心分量可用同一套$\mathbb F_{16}$坐标

正文引理5.2已经直接求和；附录A另给CMP公式(4)的实际参数对应。这样引用不是“看到同一种方法”，而是可逐项核验的同一个函数。

取

$$
E=K[\beta],\qquad\beta^2+\beta=\alpha.
$$

因为 $\operatorname{Tr}_{K/\mathbb F_2}(\alpha)=1$，方程 $w^2+w=\alpha$ 在 $K$ 无解，所以 $E$ 是 $K$ 的二次扩域，即 $\mathbb F_{16}$。它不同于第五章有幂零元的环 $R$。四元域上的非平凡共轭使 $\beta\mapsto\beta+1$，故相对迹 $\operatorname{Tr}_{E/K}(\beta)=1$，而 $\operatorname{Tr}_{E/K}(c)=0$ 对所有 $c\in K$。若 $r+s\beta\in E$，其相对迹就是 $s$。

作一次共同输入坐标及频率坐标变化：

$$
X=(b+d)+\beta d,\quad Y=a+\beta c,
\qquad U=\upsilon+\beta\sigma,
\quad V=(\tau+\rho)+\beta\rho.
$$

每个变化均可逆，例如从 $X=x_0+\beta x_1$ 恢复 $d=x_1,b=x_0+x_1$；从 $Y$ 恢复 $a,c$。它们对三个分量相同，没有给每个标量偷偷选不同坐标。

乘法公式为

$$
(r+\beta s)(u+\beta v)
=(ru+\alpha sv)+\beta(rv+su+sv).
$$

因此 $XY$ 的 $\beta$ 系数为 $(b+d)c+da+dc=bc+ad$，从而

$$
\operatorname{Tr}_{E/K}(XY)=ad+bc.
$$

同样 $UX$ 的相对迹为 $\upsilon d+\sigma b$，$VY$ 的相对迹为 $\tau c+\rho a$，故

$$
\operatorname{Tr}_{E/\mathbb F_2}(UX+VY)
=\operatorname{Tr}(\rho a+\sigma b+\tau c+\upsilon d).
$$

这精确运输了原来的Fourier配对，而不是暗中更换内积。

记

$$
\mathcal H(Y)=\operatorname{Tr}(ac)+fa+ga^2+\ell c+mc^2,
\quad Y=a+\beta c.
$$

它是一个 $K$ 值函数，不必为 $K$ 齐次二次型。对全部八系数细化，逐分量定义

$$
\begin{aligned}
h_z&=(z\theta+z^2j^2)+\beta(z\eta+z^2k^2),\\
\pi_z(Y)&=zY+h_z,
\qquad g_z(Y)=z\beta\mathcal H(Y).
\end{aligned}
$$

$z\ne0$，所以 $\pi_z$ 是 $E$ 的仿射置换。由上面的乘法，$\operatorname{Tr}_{E/K}(Xh_z)$ 恰为 $b(z\eta+z^2k^2)+d(z\theta+z^2j^2)$。再用迹对平方的恒等式以及 $\operatorname{Tr}_{E/K}(\beta\mathcal H)=\mathcal H$，得到严格恒等式

$$
\operatorname{Tr}(zQ^{(0)})
=\operatorname{Tr}_{E/\mathbb F_2}
\left(X\pi_z(Y)+g_z(Y)\right).
$$

CMP式(4)、p.313在本次**标量**使用中的参数是 $p=2,m=4,s=1$、分量参数1。这里 $z$ 已经用来标记原三个分量，不能再把它与文献中的另一个标量参数混用。原式允许任意 $g$；负号因特征2消失。先对 $X$ 求和，即得实际对偶相位

$$
\operatorname{Tr}_{E/\mathbb F_2}
\left(V\pi_z^{-1}(U)+g_z(\pi_z^{-1}(U))\right).
$$

现在

$$
\pi_z^{-1}(U)=a_z+\beta c_z,
$$

$$
a_z=\upsilon/z+\theta+zj^2,
\qquad c_z=\sigma/z+\eta+zk^2.
$$

第一项相对迹给 $\rho a_z+\tau c_z$；第二项给 $z\mathcal H(a_z+\beta c_z)$。再把平方项移到系数，正得到原稿式(5.5)，连同 $E_z(0)$ 一起保留。这一代入适用于全部 $2^{16}$ 个细化，不仅适用于筛选后的96个。

当 $\eta=\theta=j=k=0$ 时，整个 $K$ 值映射还可共同写成

$$
Q^{(0)}=\operatorname{Tr}_{E/K}
\left(XY+\beta\mathcal H(Y)\right).
$$

因此核心确实属于一般 $g\ne0$ 的MM表示，而非与MM完全无关。但CMP Theorem 2的后续闭合结论另取 $g=0$，不能从这个共同表示跳过联合筛选。此处正确区分的是“旧公式确实给出所需相位”与“旧定理是否自动给完整极值分类”，不能取其中一端代替另一端。

## 8.7 附录B：MPG特定印刷陈述的最小实例

本附录仅针对项目保存的MPG13 **19页ePrint版本，第14页Proposition 7**。该版本印刷陈述把vanishing pencil归约到特征 $(0,0,H^m,0)$，$m\ge d/2$。这里不把其他版本同编号的自同构命题混为一谈，也不据此否定整篇算法。正文主定理的自足证明不使用这个归约。

为理解例子，只需一个更小局部环：$R_0=\mathbb F_2[H]/(H^2)$，局部长度 $d=2$，$t=1+H$。它不是前面 $p(t)^2$ 的八维核心，也不属于本稿semi-extraspecial群类。令 $x=a+Hb,y=c+Hd$，$a,b,c,d\in\mathbb F_2$，并令 $\lambda(a+Hb)=b$。取

$$
q_\infty=ad+bc,\qquad
q_0=ad+bc+ac+a^2+c^2.
$$

注意二元函数中 $a^2=a$、$c^2=c$；这些对角平方项没有二次极化，却是完整函数的重要部分。把每个环坐标按 $(b,a)$、$(d,c)$ 排列，乘 $t=1+H$ 的矩阵与配对矩阵为

$$
M=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
T=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
TM=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
$$

$T,TM$ 都可逆，所以两个标量极化都非退化；$M$ 的最小多项式和特征多项式同为 $(X+1)^2$，所以是所需的循环正则primary笔。$q_\infty$ 没有对角平方项，$q_0$ 的两个对角特征为 $H,H$，完整特征为 $(0,0,H,H)$。

还需要核查原文vanishing条件，而不能只给一个任意非退化笔。可逆二元输入变化

$$
\phi(a,b,c,d)=(a,b+c,c,d+a+c)
$$

会交换两个完整函数。直接代入：

$$
q_\infty(\phi)=a(d+a+c)+(b+c)c
=ad+bc+ac+a^2+c^2=q_0.
$$

由于 $a,c$ 没变，额外的 $ac+a^2+c^2$ 再加一次便相消，所以 $q_0(\phi)=q_\infty$；并且 $\phi^2=\operatorname{id}$，可逆性也已检查。因此两个有序笔都满足semi-vanishing，正是该印刷陈述采用的vanishing条件。

接下来不需要依赖某个未证明的迹不变量，只数完整函数的共同零点。源映射同时为零先要求两式相加为零：

$$
ac+a+c=0.
$$

将 $(a,c)=(0,0),(0,1),(1,0),(1,1)$ 代入，只有 $(0,0)$ 成立。此时 $ad+bc=0$ 对 $b,d$ 没有约束，故共同零点恰为4个。

印刷目标在 $d=2,m\ge1$ 时，$H^m$ 不是 $H$ 就是0，因此目标第二式分别为

$$
ad+bc+ac+a^2,
\qquad ad+bc+ac,
$$

第一式仍为 $ad+bc$。在第一个目标，额外条件为 $ac+a=0$，允许 $(a,c)=(0,0),(0,1),(1,1)$；这三种下，$ad+bc=0$ 分别给4、2、2个 $(b,d)$，合计8个共同零点。在第二个目标，额外条件为 $ac=0$，允许 $(0,0),(0,1),(1,0)$，同样给4、2、2个，合计8个。

可逆输入换基是定义域的双射，保持共同零点数；再允许一个共同可逆目标换基，也保持“两个分量都为零”的条件。所以源的4个共同零点不可能变成目标的8个。该固定原域的同构陈述不包含扩域或改变函数的任意仿射操作，不能以那些更大的关系消除矛盾。

由此得到的是对**所保存版本和指定命题印刷陈述**的反例。它没有说其他版本相同编号的命题也错，没有检验整个算法，也不是本稿主定理原创的证据。19页版、17页会议存档和作者上传另一版的编号差别，已在项目第九轮专项记录中分别保存。公开论文保留此附录，是让特定文献说明具有可核查依据；读者可以完全不使用它来验证主定理1.1和1.2。

## 8.8 本章使用的可核对文献入口

以下列出本章直接用到的正式书目信息及版本入口。链接用于核对来源，不表示这些第三方全文属于本项目发布包，也不授予重新分发权。

- K. Abdukhalikov, R. Feng, D. Ho, *Quadratic bent functions and their duals*, Applicable Algebra in Engineering, **Communication** and Computing 35 (2024), 507—523. [DOI:10.1007/s00200-022-00564-5](https://doi.org/10.1007/s00200-022-00564-5)。刊名Communication为单数。
- A. Çeşmelioğlu, W. Meidl, A. Pott, *Vectorial bent functions and their duals*, Linear Algebra and its Applications 548 (2018), 305—320. [DOI:10.1016/j.laa.2018.03.016](https://doi.org/10.1016/j.laa.2018.03.016)。
- D. Kaur, A. Kulshrestha, *Strongly real special 2-groups*, [arXiv:1210.3790v1](https://arxiv.org/abs/1210.3790v1)。中心积对应按原始v1 PDF为Lemma 2.4，不能以其他呈现方式的编号替换。
- D. Kaur, A. Kulshrestha, *Characters of real special 2-groups*, [arXiv:1510.06583v1](https://arxiv.org/abs/1510.06583v1)。
- M. L. Lewis, J. Maglione, *Enumerating isoclinism classes of semi-extraspecial groups*, Proceedings of the Edinburgh Mathematical Society 63 (2020), 426—442. [DOI:10.1017/S0013091519000531](https://doi.org/10.1017/S0013091519000531)；本稿定理编号按[arXiv:1806.10511v2](https://arxiv.org/abs/1806.10511v2)。
- J. Plût, P.-A. Fouque, G. Macario-Rat, *Solving the “Isomorphism of Polynomials with Two Secrets” Problem for All Pairs of Quadratic Forms*, [arXiv:1406.3163v3](https://arxiv.org/abs/1406.3163v3)，特别§4、PDF pp.15—18，Propositions 4.5、4.7。
- G. Macario-Rat, J. Plût, H. Gilbert, *New Insight into the Isomorphism of Polynomial Problem IP1S and Its Use in Cryptography*, [IACR ePrint 2013/799](https://eprint.iacr.org/2013/799.pdf)。本稿附录B的对象是项目已保存19页版本，不将在线链接未来替换后的内容自动认作相同版本。
- J. Wang, F.-W. Fu, Y. Wei, *Bent Partitions, Vectorial Dual-Bent Functions and Partial Difference Sets*, [arXiv:2301.00581v1](https://arxiv.org/abs/2301.00581v1)。

本解析是辅助自行阅读的解释材料。完成这些文件，不表示作者已经读完、核验全部证明或确认原创性；内部AI核查也不等同外部同行评审。若解析与对应正式论文实际定义或推导不符，应记录具体位置交由维护稿件的主对话处理，而不在另一答疑对话中无记录地改写论文。

# 第五章　八维核心：从全部细化到一个严格同构类型

本章逐步解释原稿§5：引理5.1（基线第9—10页）、引理5.2（第10页）、引理5.3与命题5.4、5.5（第11—12页）。这里“八维”始终指商空间 $V=G/Z(G)$ 在 $\mathbb F_2$ 上的维数；相应群阶为 $4\cdot2^8=1024$。本章只分类已经满足最大自逆元素数和下界等号的八维对象。不能把固定某种极化后的计算，误当作所有八维平方映射的分类。

上一章已经构造了一个下界对象，证明下界可达。本章的问题更强：还有没有其他群同构类型？答案需要两个独立步骤：先覆盖全部可能的平方映射，再用允许的换基把全部筛选结果化到同一代表。只比较交换子映射，或只证明一个构造满足等号，都不够。

## 5.1 等号先告诉我们什么

沿用第三章的记号：$B_1,B_2$ 是两个标量极化矩阵，$A=B_1^{-1}B_2$，$p(t)=t^2+t+1$。原稿命题3.5(b)已经给出充要条件的一部分：偶数半维数下端的极化必须恰有一对 $p^2$ 循环块，其余为简单 $p$ 块对。在八维情形没有余下空间，因此恰是两个相同的 $p^2$ 循环模。

“一对 $p^2$ 块”与“两对简单 $p$ 块”不同。前者每个循环块的最小多项式是 $p^2$；后者的最小多项式只是 $p$。两种情形的特征多项式都可能是 $p^4$，但只有前者非半单。不能仅看特征多项式便将它们合并。

由引理3.3，我们能选出互相配对的两个循环子空间；每个单独对 $B_1$ 都是全迷向的，但两者之间的配对非退化。把算子 $A$ 的作用写成“乘 $t$”，这两个空间都成为

$$
R=\mathbb F_2[t]/(p^2)
$$

的一个自由秩一模，合起来为 $R^2$。$R$ 有 $2^4=16$ 个元素，$R^2$ 才是八维二元空间。这里的环不是一个有16个元素的域；它含有非零幂零元。

更高维时，同样先取这个 $R^2$ 作为 $V_0$，再取 $B_1$ 正交补 $V_1$。因为 $A$ 对 $B_1$ 自伴，若 $x\in V_0$、$y\in V_1$，则

$$
B_1(x,Ay)=B_1(Ax,y)=0.
$$

所以 $V_1$ 对 $A$ 不变，并同时与 $V_0$ 关于 $B_1,B_2$ 正交。于是这是同一个向量值极化 $B$ 的共同正交分解。这个步骤只用极化，没有推出任何限制块的原始Gauss和为正；符号要到下一章才处理。

## 5.2 为什么局部环可写成四元域加一个幂零方向

在 $R$ 中定义

$$
\varepsilon=p(t)=t^2+t+1,\qquad \alpha=t+\varepsilon=t^2+1.
$$

商去 $p^2$ 正是说 $\varepsilon^2=0$。又有

$$
\alpha^2+\alpha+1
=(t+\varepsilon)^2+t+\varepsilon+1
=p(t)+\varepsilon=0.
$$

因此 $\alpha$ 生成一个子域 $K\cong\mathbb F_4$，其中 $\alpha^2=\alpha+1$、$\alpha^3=1$。每个环元唯一写成 $a+\varepsilon b$，$a,b\in K$，故

$$
R=K[\varepsilon]/(\varepsilon^2).
$$

这是将一个四维二元计算压缩成两个四元域坐标的办法，并未把原平方映射变成 $K$ 上齐次二次型。$\varepsilon$ 记录了不能被域坐标消除的非半单部分。环元 $a+\varepsilon b$ 可逆当且仅当 $a\ne0$：若 $a\ne0$，其逆为 $a^{-1}+\varepsilon b a^{-2}$；若 $a=0$，其平方为零。

令 $\lambda:R\to\mathbb F_2$ 提取多项式代表中的 $t^3$ 系数。配对 $(x,y)\mapsto\lambda(xy)$ 非退化：非零代表 $x$ 的次数若为 $j\le3$，乘以 $t^{3-j}$ 后恰有最高项 $t^3$，还没有超过三次而发生模约化，故 $\lambda(xt^{3-j})=1$。

为什么可以把实际配对规范到这一配对？因为循环模之间的平衡配对由一个线性泛函 $\lambda'$ 决定，而 $e\mapsto[z\mapsto\lambda(ez)]$ 是两个四维二元空间间的线性同构。因此存在唯一 $e\in R$ 使 $\lambda'(z)=\lambda(ez)$。实际配对非退化迫 $e$ 可逆；否则乘 $e$ 有非零核，会成为配对的根。将一个循环生成元乘以 $e^{-1}$ 即完成规范化，没有变动目标坐标。

于是原稿式(5.3)的两个标量极化成为

$$
B((x,y),(x',y'))=
\bigl(\lambda(xy'+x'y),\lambda(t(xy'+x'y))\bigr).
$$

这里第一项是 $B_1$，第二项是 $B_2$；同一个 $t$ 在两个循环模上起作用。对应简单 $p$ 块时，$t$ 就变成乘以 $\alpha$，可用同一目标顺序的迹配对规范化。

## 5.3 从环配对得到全部平方映射

记 $\operatorname{Tr}=\operatorname{Tr}_{K/\mathbb F_2}$，即 $\operatorname{Tr}(w)=w+w^2$。四个值为

$$
\operatorname{Tr}(0)=\operatorname{Tr}(1)=0,
\qquad \operatorname{Tr}(\alpha)=\operatorname{Tr}(\alpha^2)=1.
$$

在基 $1,\alpha,\varepsilon,\alpha\varepsilon$ 上直接计算，得

$$
\lambda(a+\varepsilon b)=\operatorname{Tr}(b),\qquad
\lambda(t(a+\varepsilon b))=\operatorname{Tr}(a+\alpha b).
$$

用 $x=a+\varepsilon b$、$y=c+\varepsilon d$ 写环坐标，则 $xy=ac+\varepsilon(ad+bc)$。基准平方映射的标量值为

$$
\bigl(\operatorname{Tr}(ad+bc),\operatorname{Tr}(ac+\alpha(ad+bc))\bigr).
$$

原稿固定目标识别 $\iota(w)=(\operatorname{Tr}(w),\operatorname{Tr}(\alpha w))$。若将上述有序对写回 $K$，其值正是

$$
Q_{\mathrm{base}}=ad+bc+\operatorname{Tr}(ac).
$$

可核对第二分量：$\operatorname{Tr}(\alpha\operatorname{Tr}(ac))=\operatorname{Tr}(ac)$，因为 $\operatorname{Tr}(ac)\in\mathbb F_2$ 且 $\operatorname{Tr}(\alpha)=1$。

现在必须补齐所有与基准映射有同一极化的映射。若 $Q,Q_0$ 的极化相同，$L=Q+Q_0$ 满足 $L(x+y)=L(x)+L(y)$；在二元空间上这恰是线性。因此全部细化是 $Q_0+L$，不能只选最方便的一种。

每个二元线性映射 $K\to K$ 都唯一写成 $a\mapsto fa+ga^2$，$f,g\in K$。这是因为 $a\mapsto a^2$ 在 $\mathbb F_2$ 上线性；若 $fa+ga^2$ 恒零，代 $a=1$ 得 $f=g$，再代 $a=\alpha$ 得 $f(\alpha+\alpha^2)=f=0$。这给一个四维二元空间到另一个四维二元空间的单射，所以也是满射。

独立作用于 $a,b,c,d$ 四个坐标，便得到原稿式(5.1)的完整列表：

$$
\begin{aligned}
Q^{(0)}={}&ad+bc+\operatorname{Tr}(ac)
+fa+ga^2+\ell c+mc^2\\
&+\eta b+kb^2+\theta d+jd^2,
\end{aligned}
$$

八个系数都在 $K$，共有 $4^8=2^{16}$ 个带坐标映射。这里 $ga^2$ 虽然写成平方，却也是二元线性项；$fa$ 虽然是普通一次项，却不能被任意删掉。所有这些映射共有极化，未必有相同的零点数、四元子群数或群同构类型。

## 5.4 全部核心相位：先算Walsh和，不先假定正号

引理5.2评价所有上述候选。三个非零标量分量用 $z\in K^\times$ 标记，取 $q_z=\operatorname{Tr}(zQ^{(0)})$。频率为

$$
\operatorname{Tr}(\rho a+\sigma b+\tau c+\upsilon d).
$$

这个非退化迹配对表示全部二元线性泛函，没有遗漏频率。令 $\kappa_z=\operatorname{Tr}(z)$。先用

$$
\operatorname{Tr}(zb^2k)=\operatorname{Tr}(z^2k^2b)
$$

把平方项移入 $b$ 的线性系数。恒等式来自 $\operatorname{Tr}(w)=\operatorname{Tr}(w^2)$ 及 $b^4=b$。因此在固定 $a,c$ 后，$b$ 的系数为

$$
zc+z\eta+z^2k^2+\sigma.
$$

对 $b\in K$ 求和：这个系数非零时和为零，系数为零时和为4。同理，$d$ 的系数为 $za+z\theta+z^2j^2+\upsilon$。故全部求和只留下

$$
a=a_z=\upsilon/z+\theta+zj^2,
\qquad c=c_z=\sigma/z+\eta+zk^2,\tag{\text{原稿 5.4}}
$$

并产生 $4\cdot4=16$ 倍率。剩余指数给

$$
\mathcal W_z=16(-1)^{E_z},
$$

$$
E_z=\operatorname{Tr}\left(
\kappa_z a_zc_z+(\rho+zf+z^2g^2)a_z
+(\tau+z\ell+z^2m^2)c_z\right).\tag{\text{原稿 5.5}}
$$

尤其 $E_z(0)$ 是原始Gauss和的符号：为0才是正16，为1则是负16。不能先把它减掉，再声称三个块都为正。此直接求和也是CMP2018式(4)的坐标代入；附录讲解会说明三个分量使用的共同 $\mathbb F_{16}$ 坐标。

将三个 $E_z$ 在 $\mathbb F_2$ 中相加，可以把许多项消去。为让式(5.6)可独立核查，列出实际需要的有限和：$K^\times=\{1,\alpha,\alpha^2\}$，所以

$$
\sum z=\sum z^2=\sum z^{-1}=0,\quad
\sum z^3=1,\quad \sum\kappa_z=0,
$$

$$
\sum\kappa_z/z=\sum\kappa_z/z^2
=\sum\kappa_z z=\sum\kappa_z z^2=1.
$$

例如 $\kappa_1=0$、$\kappa_\alpha=\kappa_{\alpha^2}=1$，故 $\sum\kappa_z/z=\alpha^2+\alpha=1$。这些和在特征2的域内进行，三个1之和是1。

展开 $\kappa_z a_zc_z$ 后，求和保留下来的是

$$
\sigma\upsilon+\eta\upsilon+\theta\sigma
+\theta k^2+\eta j^2+j^2k^2.
$$

展开 $(\rho+zf+z^2g^2)a_z$ 后保留下来的是 $\theta\rho+f\upsilon+g^2j^2$；另一项同理给 $\eta\tau+\ell\sigma+m^2k^2$。再用迹不随平方改变，得到

$$
\begin{aligned}
D_0:=\sum_{z\ne0}E_z
={}&\operatorname{Tr}\bigl(\sigma\upsilon+(f+\eta)\upsilon
+(\ell+\theta)\sigma+\theta\rho+\eta\tau\bigr)+\gamma,\\
\gamma={}&\operatorname{Tr}(\theta k^2+\eta j^2+jk+gj+mk)
=\sum_{z\ne0}E_z(0).
\end{aligned}\tag{\text{原稿 5.6—5.7}}
$$

这里 $D_0$ 是相位函数，不是整数字符和。作为区分的教学例，八维空间上的常数1函数的字符和是 $-256$，而不是1或0；这不是说本段固定极化的 $D_0$ 能成为常数函数，其极化秩始终为4。下一章中 $D_0$ 还可能含不能先删的常数 $\gamma$。

## 5.5 各向异性为什么能阻止某些原点符号

引理5.3先作一个条件性推论。设 $\eta=\theta=0$，并且三个原始Gauss和具有同一个符号 $(-1)^\delta$。这里尚允许 $\delta=1$。在零频处 $a_z=zj^2,c_z=zk^2$。置

$$
e=jk,\qquad u=fj^2+\ell k^2,\qquad v=gj+mk.
$$

从式(5.5)得到

$$
E_z(0)=\operatorname{Tr}(z)\operatorname{Tr}(ze)
+\operatorname{Tr}(z^2u)+\operatorname{Tr}(v).
$$

其中 $z^3=1$ 把 $g,m$ 项变成常数；$\operatorname{Tr}(z^2e^2)=\operatorname{Tr}(ze)$ 处理了第一项。为核查原稿的再化简，可在 $K$ 内展开

$$
\begin{aligned}
\operatorname{Tr}(z)\operatorname{Tr}(ze)
&=(z+z^2)(ze+z^2e^2)\\
&=z^2e+ze^2+e+e^2\\
&=\operatorname{Tr}(z^2e)+\operatorname{Tr}(e).
\end{aligned}
$$

故

$$
E_z(0)=\operatorname{Tr}(z^2(u+e))+
\operatorname{Tr}(v+e).
$$

若 $u+e\ne0$，第一项是 $z$ 的一个非零二元线性泛函，在三个非零域元上不可能为常数：非零泛函的核有两个元素，其中恰一个非零，另外两个非零域元取值1。因此三个相位全相同恰好等价于

$$
fj^2+\ell k^2=jk,
\qquad \operatorname{Tr}(gj+mk+jk)=\delta.\tag{\text{原稿 5.8}}
$$

现在加上 $\operatorname{Tr}(f\ell)=1$。它推出 $f,\ell\ne0$，且 $K$ 上二元齐次型

$$
fX^2+XY+\ell Y^2
$$

没有非零零点，也就是各向异性。证明不必背诵Arf分类：若 $Y=0$，方程迫 $X=0$；若 $Y\ne0$，令 $w=fX/Y$，将方程乘以 $f/Y^2$ 后得到 $w^2+w+f\ell=0$。但 $\operatorname{Tr}(w^2+w)=0$，与 $\operatorname{Tr}(f\ell)=1$ 矛盾。

把 $(X,Y)=(j,k)$ 代入，式(5.8)便迫 $j=k=0$；第二式随即迫 $\delta=0$。这是一条条件清楚的限制：各向异性是在下端负字符和出现后才得到的，不能仅由整体最大自逆元素数便引用它。

## 5.6 为什么恰好96个，而且没有漏掉其他细化

命题5.4把上面几步按正确顺序联立。八维下界等号要求 $s=304$、$v_4=4371$。其必要性如下。

首先，命题3.5已经保证所有对象的极化都是本章这一对 $p^2$ 块，所以式(5.1)确实覆盖全部对象。其次，最大 $s$ 意味着三个 $E_z(0)$ 都是0，从而 $\gamma=0$。式(5.6)的二次部分只有 $\operatorname{Tr}(\sigma\upsilon)$，故其极化根恰为 $\rho,\tau$ 两个 $K$ 方向，也就是四维二元根。$D_0$ 在根上消失要求

$$
\operatorname{Tr}(\theta\rho+\eta\tau)=0
\quad\text{对所有 }\rho,\tau\in K.
$$

迹配对非退化，于是 $\theta=\eta=0$。这里不能只检查 $\rho=\tau=1$，那会漏掉迹为零但非零的系数；必须对全部域元成立。

此时对 $D_0$ 求整数字符和，$\rho,\tau$ 自由给出16倍；再先对 $\sigma$ 求和：

$$
\begin{aligned}
\sum_{\rho,\sigma,\tau,\upsilon}(-1)^{D_0}
&=16\sum_{\sigma,\upsilon}
 (-1)^{\operatorname{Tr}(\sigma\upsilon+f\upsilon+\ell\sigma)}\\
&=16\cdot4\,(-1)^{\operatorname{Tr}(f\ell)}\\
&=64(-1)^{\operatorname{Tr}(f\ell)}.
\end{aligned}\tag{\text{原稿 5.10}}
$$

第二行的原因是：对 $\sigma$ 的和在 $\upsilon=\ell$ 时等于4，其他三个 $\upsilon$ 时均为0。下端要求字符和为 $-64$，因此 $\operatorname{Tr}(f\ell)=1$。引理5.3再以 $\delta=0$ 迫 $j=k=0$。于是全部等号细化只能是

$$
Q_{f,g,\ell,m}=ad+bc+\operatorname{Tr}(ac)+fa+ga^2+\ell c+mc^2,
\qquad \operatorname{Tr}(f\ell)=1.\tag{\text{原稿 5.9}}
$$

反方向也要检查：这些映射在零频处 $a_z=c_z=0$，故三个原始相位均为0；上式的字符和确为 $-64$。所有极化保持非退化，原稿的计数恒等式于是给出

$$
v_4=M_4+\frac{2^4}{4}(-64)=4627-256=4371.
$$

因此列出的不只是必要候选，确实个个满足要求。计数时 $f$ 有3个非零选择；每个 $f$ 下有2个 $\ell$ 使 $f\ell\in\{\alpha,\alpha^2\}$；$g,m$ 各4种。因此共 $3\cdot2\cdot4\cdot4=96$。

**96是固定极化、固定坐标中的映射数，不是群同构类型数。** 全部 $2^{16}$ 候选到96的缩减靠充要条件完成，不靠“程序没找到别的”。下一步才比较这96个之间的严格等价。

## 5.7 四次显式输入换基如何给出传递性

命题5.5要证明它们全都等价于

$$
Q_*=ad+bc+\operatorname{Tr}(ac)+a+\alpha c.
$$

原稿使用 $\operatorname{SL}_2(R)$ 作用于列向量 $(x,y)^{\mathsf T}$，$x=a+\varepsilon b$、$y=c+\varepsilon d$。对任意二阶矩阵，交替表达式 $xy'+x'y$ 在换基后乘以行列式；行列式为1便同时保持式(5.3)的两个标量极化。下面每一步都是对完整映射作拉回，即计算 $Q(M(x,y))$，不是任意添加一个线性映射。

第一步取

$$
M_1=\begin{pmatrix}1&\varepsilon m\\ \varepsilon g&1\end{pmatrix}.
$$

其行列式为 $1+\varepsilon^2mg=1$，所以可逆。它使 $a,c$ 不变，而 $b\mapsto b+mc$、$d\mapsto d+ga$。基准项变成

$$
a(d+ga)+(b+mc)c+\operatorname{Tr}(ac)
=ad+bc+\operatorname{Tr}(ac)+ga^2+mc^2.
$$

这两个新项恰与原有 $ga^2+mc^2$ 相消。于是 $g,m$ 被消去。注意相消来自实际拉回的基准项；如果未经说明就“忽略线性项”，无法得到严格等价。

第二步取 $M_2=\operatorname{diag}(f^{-1},f)$。它将 $a,b$ 乘 $f^{-1}$，$c,d$ 乘 $f$。三个基准项均不变，$fa$ 变成 $a$，$\ell c$ 变成 $f\ell c$。迹一条件只剩 $f\ell=\alpha$ 或 $\alpha^2$。

若已经为 $\alpha$，便得到 $Q_*$。若为 $\alpha^2$，第三步取

$$
M_3=\begin{pmatrix}1&\alpha\\0&1\end{pmatrix}.
$$

这给 $a\mapsto a+\alpha c$、$b\mapsto b+\alpha d$，另两坐标不变。$ad+bc$ 的两个额外 $\alpha cd$ 相消，但

$$
\operatorname{Tr}((a+\alpha c)c)
=\operatorname{Tr}(ac)+\alpha c^2+\alpha^2c.
$$

再加 $a+\alpha c$ 及原来的 $\alpha^2c$，普通 $c$ 项的系数成为 $\alpha^2+\alpha+\alpha^2=\alpha$，另留下 $\alpha c^2$。最后用

$$
M_4=\begin{pmatrix}1&\varepsilon\alpha\\0&1\end{pmatrix}
$$

使 $b\mapsto b+\alpha c$，基准项多出 $\alpha c^2$，恰好消掉残项。这四步的目标变换始终是 $T=\operatorname{id}_W$。

因此，对96个映射中的每一个，已经写出一条通向 $Q_*$ 的可核查路径。这是传递性证明，不需要先枚举完整变换群，也不需要以“不变量相同”代替同构证明。

## 5.8 变换群、具体群与本章的逻辑终点

原稿注5.6还说明固定两个标量极化的全体等距群就是 $\operatorname{SL}_2(R)$。保持两个极化的变换必与 $A=B_1^{-1}B_2$ 交换，故是 $R$ 线性的。若其行列式为 $d$，第一极化的保持要求 $\lambda((d-1)r)=0$ 对所有 $r\in R$ 成立；非退化配对迫 $d=1$。一个可作为可逆矩阵首列的列向量必须至少有一个单位坐标，故有 $16^2-4^2=240$ 种；对每个首列，行列式映射满射到 $R$，每个纤维16元，于是群阶为 $240\cdot16=3840$。

这个群阶计算是补充核对，不承担前面的轨道穷尽性。即使再允许目标换基，也不能把已经同属一个较小群轨道的96个映射拆开。

最后，原稿式(5.11)给出不依赖抽象存在性的群乘法。取集合 $K^4\times K$，令

$$
F(v,v')=ad'+bc'+\operatorname{Tr}(ac')+(aa')^2+\alpha(cc')^2.
$$

它在二元意义下双线性；例如 $(aa')^2$ 对 $a,a'$ 各自加法可加。取对角得 $a^4=a$、$c^4=c$，故 $F(v,v)=Q_*(v)$。按原稿式(2.1)定义 $(v,w)(v',w')=(v+v',w+w'+F(v,v'))$，得到阶1024的 $G_*$。三个标量极化非退化，是因为 $1,t,1+t$ 均为 $R$ 的单位。因此命题2.1保证它确属要求的群类。

至此八维分类的四项任务都已闭合：所有下端极化纳入模型，全部细化纳入候选，充要条件筛出96个，显式严格换基将它们合并为一个群同构类型。这里的局部环、相位公式与Arf判据是已有工具；本文保留的研究对象是这些工具合成后的具体极值分类，而不是新的通用二次型理论。

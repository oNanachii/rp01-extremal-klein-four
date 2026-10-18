# 4 每个端点都真实存在：四维、六维与八维构造

本章对应英文第4节，基线第7—9页：引理4.1、4.2、4.3及定理1.1的完成证明。上一章给的是“任何群不能越过的界”。本章必须构造函数并核对：三个标量极化非退化、三个原始Gauss和全正、第三矩有精确数值。命题2.1才能据此造出满足全部群假设的群。构造不依赖后面的唯一性分类，因而避免循环论证。

## 4.1 一个会反复使用的求和方法

令 $L=\mathbb F_{2^m}$，$\operatorname{Tr}_L$ 为到 $\mathbb F_2$ 的绝对迹，且 $a\ne0$。考虑

$$
\sum_{x,y\in L}(-1)^{\operatorname{Tr}_L(axy+cx+dy+ux+vy)}.
$$

对固定 $x$ 先对 $y$ 求和，$y$ 的系数是 $ax+d+v$。迹配对非退化，所以该内和仅在 $ax+d+v=0$ 时非零，非零值是 $2^m$。唯一满足的 $x$ 为 $(v+d)/a$，故总和等于

$$
2^m(-1)^{\operatorname{Tr}_L((u+c)(v+d)/a)}.
\tag{英文(4.2)，在本章所用的维数下}
$$

这既算出了原始Gauss符号（令 $u=v=0$），又算出全部实际Walsh对偶（保留 $u,v$）。它是一般Maiorana–McFarland公式[CMP18，式(4)，印刷页313]的直接实例；任意辅助函数 $g$ 的一般式会在后续相位计算及附录中用到。当前不把这条经典求和方法说成新方法。

## 4.2 引理4.1：四维正端块 $H_+$

取 $K=\mathbb F_4$，$\alpha^2+\alpha+1=0$，$\operatorname{Tr}(w)=w+w^2$。有

$$\operatorname{Tr}(0)=\operatorname{Tr}(1)=0,\qquad
\operatorname{Tr}(\alpha)=\operatorname{Tr}(\alpha^2)=1.$$

英文(4.1)用

$$\iota(w)=(\operatorname{Tr}(w),\operatorname{Tr}(\alpha w))$$

把 $W=K$ 识别为 $\mathbb F_2^2$。非零分量可统一写作 $q_z=\operatorname{Tr}(zQ)$，其中 $z\in K^\times$；$z=1,\alpha,\alpha^2$ 恰对应三个非零泛函。这是一组共同的目标坐标，后面拼接各块始终保留它。

对 $H_+(u,v)=uv$，极化为 $uv'+u'v$，标量极化是 $\operatorname{Tr}(z(uv'+u'v))$。若 $u\ne0$，可选 $v'$ 使 $\operatorname{Tr}(zuv')\ne0$；若 $u=0,v\ne0$ 则交换角色，所以每个 $z\ne0$ 都非退化。

频率变量使用同一迹配对 $\operatorname{Tr}(\rho u+\sigma v)$。上一节求和给

$$
\sum_{u,v\in K}(-1)^{\operatorname{Tr}(zuv+\rho u+\sigma v)}
=4(-1)^{\operatorname{Tr}(\rho\sigma/z)}.
$$

零频都为 $+4$，所以该块达到最大 $s$。三个对偶之和为

$$D(\rho,\sigma)=\operatorname{Tr}\left(\rho\sigma\sum_{z\in K^\times}z^{-1}\right)=0,$$

因为 $K^\times$ 的逆仍是 $1,\alpha,\alpha^2$，和为0。因此 $\mathcal G(D)=16$，$h=4$，

$$\mathcal P=4^3\cdot16=2^{10}.$$

这不是依靠“正端”名称假定符号，而是完整计算。群阶为 $4\cdot16=64$，$s=16+3\cdot4=28$。

零点也很直观：$uv=0$ 当且仅当 $u=0$ 或 $v=0$，所以两条 $K$ 坐标轴各4点、相交于零，共 $z=7$ 点。它们也是仅有的两个二维二元全零子空间。若一个全零子空间含两条轴各自的非零向量，它们的和两坐标非零，乘积非零，矛盾。于是 $L=2$，第2章公式给

$$v_4=16\cdot2+6\cdot7-5=69.$$

## 4.3 同极化但不同群：$uv+u$ 给 $n=2$ 下端

考虑 $Q'(u,v)=uv+u=u(v+1)$。添加一次项不改变极化，所以三个标量极化仍非退化。其 $z$ 分量是在上一求和式中把 $\rho$ 替换为 $\rho+z$，故零频仍全正；实际对偶为

$$q_z^*(\rho,\sigma)=\operatorname{Tr}((\rho+z)\sigma/z).$$

三个相加，含 $\rho\sigma$ 的部分仍消掉，而每项留下 $\operatorname{Tr}(\sigma)$，三次相加在特征2里还是它。因此

$$D(\rho,\sigma)=\operatorname{Tr}(\sigma),$$

非零线性、极化为零、整数字符和为零。这正好实现命题3.5的 $n=2$ 下端条件。

直接零点计数也可独立核对。零集由 $u=0$ 的4点和 $v=1,u\ne0$ 的3点组成，共7点。唯一全零二维二元子空间是 $u=0$：如果含两个不同的第二类点 $(u,1),(u',1)$，其和 $(u+u',0)$ 不为零点；如果含一个第二类点与非零的 $(0,v)$，其和的 $Q'$ 值为 $uv\ne0$。所以 $L=1$，

$$v_4=16+42-5=53.$$

两个映射拥有相同的极化、相同的 $s=28$，但 $v_4$ 不同，故对应群不同构。这是全文最小、最具体的例子，说明不能在平方映射分类时任意抹去线性项。此处用零点计数与字符和两种方法算同一个结果，是对转换接口的核对，不是另一个原创主张。

## 4.4 引理4.2：为什么奇数分支需要一个六维块

奇数半维数端点的极化必须含一对简单不可约三次块。因此自然用 $L=\mathbb F_8$ 的乘法。写

$$L=\mathbb F_2[t]/(t^3+t+1),\qquad t^3=t+1,$$

且 $\operatorname{Tr}_8(w)=w+w^2+w^4$。在 $L^2$（二元维数6）上取两分量

$$q_1(x,y)=\operatorname{Tr}_8(xy),\qquad
q_2(x,y)=\operatorname{Tr}_8(txy+cx+dy).$$

第三分量是它们的函数和，二次乘积系数为 $1+t$。$1,t,1+t$ 全非零，所以三个标量极化都非退化。此处输出仍是两维二元空间；没有把 $L$ 本身误当中心，也没有把中心扩到8个元素。

先列会用到的幂，便于逐项核查：

$$
\begin{array}{c|ccccc}
j&3&4&5&6&7\\\hline
t^j&t+1&t^2+t&t^2+t+1&t^2+1&1
\end{array}
$$

所以 $t^{-1}=t^6$，$(1+t)^{-1}=t^4$，并且

$$k=t^{-1}+(1+t)^{-1}=t+1,\qquad 1+k=t.$$

迹值为 $\operatorname{Tr}_8(1)=1$、$\operatorname{Tr}_8(t)=\operatorname{Tr}_8(t^2)=0$。

当 $c=d=0$，三个原始和由求和式都是 $+8$。实际对偶相加得

$$D(u,v)=\operatorname{Tr}_8\bigl((1+t^{-1}+(1+t)^{-1})uv\bigr)=\operatorname{Tr}_8(tuv).$$

这是非退化六维二次函数，字符和为 $+8$。故 $\mathcal P=8^3\cdot8=2^{12}$，实现奇数分支最小维数 $n=3$ 的上端。

## 4.5 六维负端：逐项保留原始相位

现在取

$$c=1,\qquad d=t^2+t+1=t^5.$$

不能因为极化未变就断言原始Gauss和仍正；需检查两项可能的原点相位：

$$\operatorname{Tr}_8(cd/t),\qquad\operatorname{Tr}_8(cd/(1+t)).$$

由幂表，$d/t=t^4=t^2+t$，$d/(1+t)=t^2$，迹均为0。因此三个原始和确实都是 $+8$。按同一频率配对，三个实际对偶完整相加为

$$D(u,v)=\operatorname{Tr}_8(tuv+kdu+kcv+kcd).$$

这里的常数 $kcd$ 是对偶公式实际给出的项；即使最后其迹为零，也应在代入前保留，避免把块级原点相位混淆。应用求和式，

$$
\mathcal G(D)=8(-1)^{\operatorname{Tr}_8(cd(k+k^2/t))}.
$$

因为 $k=t+1$，特征2下 $k^2=t^2+1$，所以

$$k+k^2/t=k/t=t^2.$$

而 $(k/t)d=t^2t^5=t^7=1$，迹是1，故

$$\mathcal G(D)=-8,\qquad \mathcal P=8^3(-8)=-2^{12}.$$

$D$ 的极化由系数 $t$ 给出，依然非退化。这个例子把“原来的三个和全正”与“它们实际对偶相加后的和为负”清楚分开：二者并不矛盾。数值上 $M_3=447$，偏移 $2^{3\cdot3-5}=16$，得到上下端431与463。

## 4.6 引理4.3：八维负端为什么使用 $p^2$ 局部环

偶数下端等号要求一对 $p^2$ 块，$p(t)=t^2+t+1$。取局部环

$$R=\mathbb F_2[t]/(p(t)^2),$$

它的二元维数是4。令 $U$ 为乘 $t$ 的线性变换，$E=p(U)=U^2+U+I$。在这个环中 $p^2=0$，故 $E^2=0$；但 $E\ne0$。乘 $p$ 的像和核都恰好是理想 $(p)$，维数2，所以

$$\operatorname{rank}E=2,\qquad \operatorname{im}E=\ker E.$$

这是非半单块：存在非零幂零部分 $E$。与两个简单 $p$ 块的直和相比，后者满足 $p(U)=0$，这里却不满足；特征多项式相同不代表等价。

选 $0\ne c\in\operatorname{im}E$，再选列向量 $z$ 使 $z^{\mathsf T}c=1$，置 $d=E^{\mathsf T}z$。这些选择总存在：非零向量总能被某个线性泛函取到1。$c\in\operatorname{im}E$ 又给 $Ec=0$。

在两个四维二元空间上定义

$$q_1(x,y)=x^{\mathsf T}y,\qquad
q_2(x,y)=x^{\mathsf T}Uy+c^{\mathsf T}x+d^{\mathsf T}y.$$

相应三极化的乘积系数是 $I,U,I+U$。由于 $t$ 与 $t+1$ 都和 $p^2$ 互素，它们在 $R$ 中是单位，故 $U,I+U$ 可逆。这证明三个标量极化非退化。

**教学补充例：原构造的一组具体坐标。** 在多项式基 $1,t,t^2,t^3$ 下有

$$
U=\begin{pmatrix}0&0&0&1\\1&0&0&0\\0&1&0&1\\0&0&1&0\end{pmatrix},
$$

因为 $t^4=t^2+1$。可取 $c=(1,1,1,0)^{\mathsf T}=E(1,0,0,0)^{\mathsf T}$、$z=(1,0,0,0)^{\mathsf T}$、$d=(1,0,1,1)^{\mathsf T}$。这是原构造的一个坐标实现，仅为便于直接核查，并不声称带来了新的群类型。

## 4.7 八维块的原始正号及完整对偶和

一般的二元矩阵求和与有限域求和一样：若 $M$ 为可逆四阶矩阵，则

$$
\sum_{x,y\in\mathbb F_2^4}
(-1)^{x^{\mathsf T}My+c^{\mathsf T}x+d^{\mathsf T}y+a^{\mathsf T}x+b^{\mathsf T}y}
=16(-1)^{(b+d)^{\mathsf T}M^{-1}(a+c)}.
$$

令频率为零，两项可能的原始相位是 $d^{\mathsf T}U^{-1}c$ 与 $d^{\mathsf T}(I+U)^{-1}c$。因 $d^{\mathsf T}=z^{\mathsf T}E$，$E$ 与 $U$ 及其可逆多项式都交换，且 $Ec=0$，这两项都为0。例如

$$d^{\mathsf T}U^{-1}c=z^{\mathsf T}EU^{-1}c=z^{\mathsf T}U^{-1}Ec=0.$$

所以三个原始和都是 $+16$。至此才可使用最大 $s$ 分支下无原点相位的全局对偶记号。

令 $K_0=U^{-1}+(I+U)^{-1}$。因为

$$U(I+U)=U+U^2=I+E,\qquad (I+E)^{-1}=I+E,$$

有 $K_0=(U(I+U))^{-1}=I+E$，所以

$$I+K_0=E,\quad K_0c=c,\quad EK_0=E.$$

频率 $(a,b)$ 下，三个实际对偶相加，先不删线性和常数项，得到

$$
\begin{aligned}
D(a,b)
&=b^{\mathsf T}a+(b+d)^{\mathsf T}U^{-1}(a+c)
 +(b+d)^{\mathsf T}(I+U)^{-1}(a+c)\\
&=b^{\mathsf T}(I+K_0)a+b^{\mathsf T}K_0c
  +d^{\mathsf T}K_0a+d^{\mathsf T}K_0c\\
&=b^{\mathsf T}(Ea+c)+z^{\mathsf T}Ea.
\end{aligned}
$$

最后一行使用 $d^{\mathsf T}K_0=z^{\mathsf T}EK_0=z^{\mathsf T}E$，且常数 $d^{\mathsf T}K_0c=z^{\mathsf T}Ec=0$。这说明原证明中的简式包含了全部线性与常数项的真实消去过程，不是任意减去对偶常数。

现在求和时先对 $b$。若 $Ea+c\ne0$，内和为0；若 $Ea=c$，内和为16。由于 $c\in\operatorname{im}E$，这个方程有 $|\ker E|=4$ 个解。在这些解上

$$z^{\mathsf T}Ea=z^{\mathsf T}c=1.$$

所以每个解给负号，

$$\mathcal G(D)=-16\cdot4=-64,\qquad
\mathcal P=16^3(-64)=-2^{18}.$$

还可直接核对等号的根条件：$D$ 的二次部分是 $b^{\mathsf T}Ea$，极化矩阵为 $\begin{pmatrix}0&E^{\mathsf T}\\E&0\end{pmatrix}$，秩4、根维数4。在根上有 $Ea=0,E^{\mathsf T}b=0$；又 $c\in\operatorname{im}E$，所以 $b^{\mathsf T}c=0$，即 $D$ 在根上为零。商四维的字符和是 $-64/2^4=-4$，恰符合命题3.5(b)。

因此这个8维映射实现 $n=4$ 的下端。此刻无需知道它与第1章写出的 $Q_*$ 严格等价；那是后面完整分类将证明的内容。把可达性与分类分开，是证明组织的重要逻辑边界。

## 4.8 用共同目标正交和得到全部允许维数

若 $Q=Q_0\perp Q_1$，对同一个目标泛函 $\lambda$ 有 $q_\lambda(x_0,x_1)=q_{\lambda,0}(x_0)+q_{\lambda,1}(x_1)$。频率也按直和分解，有限和直接拆开：

$$\mathcal W_\lambda(\xi_0,\xi_1)
=\mathcal W_{\lambda,0}(\xi_0)\mathcal W_{\lambda,1}(\xi_1).$$

所以原始Gauss和相乘。对三个分量乘积再对全部频率求和，仍可分离，得到

$$\mathcal P(Q_0\perp Q_1)=\mathcal P(Q_0)\mathcal P(Q_1).$$

共同目标很重要：这不是允许各块独立重新标号后再不加说明地相乘。当前每块都已经用同一有序二维目标构造，故可以直接拼接。

**偶数上端。** $n/2$ 个 $H_+$ 块共有 $4(n/2)=2n$ 维，原始和乘成 $4^{n/2}=2^n=h$，而

$$\mathcal P=(2^{10})^{n/2}=2^{5n}.$$

这也是[CMP18, Theorem 2(i)，印刷页314]的标准迹乘积构造：取输入域 $\mathbb F_{2^n}$、子域 $K=\mathbb F_4$、$\pi(y)=y$、$g=0$，映射 $\operatorname{Tr}_{\mathbb F_{2^n}/K}(xy)$ 在一对迹对偶的 $K$ 基中就是 $H_+^{\perp n/2}$。$2\mid n$ 是子域存在所需条件，不能在奇数 $n$ 无条件使用。

**奇数两个端点。** 取六维正块或负块，再加 $(n-3)/2$ 个 $H_+$。维数为 $6+4(n-3)/2=2n$，原始和乘成 $8\cdot4^{(n-3)/2}=h$，且

$$\mathcal P=\pm2^{12}\,2^{10(n-3)/2}=\pm2^{5n-3}.$$

**偶数下端。** 取八维负块，再加 $(n-4)/2$ 个 $H_+$，维数为 $2n$，原始和是 $16\cdot4^{(n-4)/2}=h$，而

$$\mathcal P=-2^{18}\,2^{10(n-4)/2}=-2^{5n-2}.$$

**$n=2$。** 已由 $uv$ 与 $uv+u$ 分别给69和53。

每个构造的标量极化都为非退化块的正交和，因而仍非退化；命题2.1给实际semi-extraspecial群，且 $Z=G'=\Phi\cong C_2^2$。原始和全正保证最大 $s$，$\mathcal P$ 的数值配合英文(3.2)保证恰到所述端点。这就同时证明群类在每个 $n\ge2$ 非空，以及定理1.1全部界是最优且可达。

接下来要解决的不是再扩大构造，而是反向穷尽：任何偶数下端等号映射，是否都能化成已指定的八维 $Q_*$ 与正余块？上一章已经把极化限制到一个 $p^2$ 对及若干简单 $p$ 对；后续必须保留每个线性细化，才能从这个极化结构走到真正的群同构结论。

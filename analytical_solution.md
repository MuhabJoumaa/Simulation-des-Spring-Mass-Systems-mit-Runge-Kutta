$$
\frac{d^2x(t)}{dt^2}=-\frac{k}{m}x(t),
\qquad k=5,\quad m=1
$$

$$
\Rightarrow\frac{d^2x(t)}{dt^2}+5x(t)=0
$$

$$
x(0)=x_0=0,\qquad x'(0)=v_0=3
$$

$$
x=e^{\lambda t}
$$

$$
\Rightarrow\frac{d^2}{dt^2}(e^{\lambda t})+5e^{\lambda t}=0
$$

$$
\Rightarrow\lambda^2e^{\lambda t}+5e^{\lambda t}=0
$$

$$
\Leftrightarrow e^{\lambda t}(\lambda^2+5)=0
$$

$$
e^{\lambda t}\neq0
\Rightarrow\lambda^2+5=0
$$

$$
\Rightarrow\lambda=\pm i\sqrt{5}
$$

$$
x_1(t)=C_1e^{i\sqrt{5}t},
\qquad
x_2(t)=C_2e^{-i\sqrt{5}t}
$$

$$
x(t)=C_1e^{i\sqrt{5}t}+C_2e^{-i\sqrt{5}t}
$$

$$
\Leftrightarrow x(t)=
C_1(\cos(\sqrt{5}t)+i\sin(\sqrt{5}t))
$$

$$
+C_2(\cos(\sqrt{5}t)-i\sin(\sqrt{5}t))
$$

$$
\Leftrightarrow x(t)=
(C_1+C_2)\cos(\sqrt{5}t)
+i(C_1-C_2)\sin(\sqrt{5}t)
$$

$$
\Rightarrow x(t)=
C_1\cos(\sqrt{5}t)+C_2\sin(\sqrt{5}t)
$$

$$
x(0)=0
\Rightarrow C_1\cos(0)+C_2\sin(0)=0
$$

$$
\Rightarrow C_1=0
$$

$$
x'(t)=-\sqrt{5}C_1\sin(\sqrt{5}t)
+\sqrt{5}C_2\cos(\sqrt{5}t)
$$

$$
x'(0)=3
\Rightarrow \sqrt{5}C_2=3
$$

$$
\Rightarrow C_2=\frac{3}{\sqrt{5}}
$$

$$
\boxed{x(t)=\frac{3}{\sqrt{5}}\sin(\sqrt{5}t)}
$$

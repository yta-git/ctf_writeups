import sympy as sp
from math import gcd

def lcm(p, q):
    return p * q // gcd(p, q)

def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        m = c0 % c1
        q = c0 // c1

        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)

    return c0, a0, b0

N = 22255382023772668851018179427844169178508638456713544208965498667359965716247243217931028270320680101854437928939452335472153643094266035953797432826168426002458800906764442624308120284177094975740468163835305872963635678413995878812492729432260346481442092245748885202467992527408086207041964831622724073720751839241897580988210971776031098476500998975223039782371635291859483569580516707907602619018780393060215756966917504096971372578145138070121288608502379649804953835336933545368863853793291348412017384228807171466141787383764812064465152885522264261710104646819565161405416285530129398700414912821358924882993
M = 455054308184393892678058040417894434538147052966484655368629806848690951585316383741818991249942897131402174931069148907410409095241197004639436085265522674198117934494409967755516107042868190564732371162423204135770802585390754508661199283919569348449653439331457503898545517122035939648918370853985174413495
e = 65537
c = 17228720052381175899005296327529228647857019551986416863927209013417483505116054978735086007753554984554590706212543316457002993598203960172630351581308428981923248377333772786232057445880572046104706039330059467410587857287022959518047526287362946817619717880614820138792149370198936936857422116461146587380005750298216662907558653796277806259062461884502203484610534512552197338982682870358910558302016481352035443274153409114492025483995668048818103066011831955626539382173160900595378864729936791103356604330731386911513668727994911216530875480647283550078311836214338646991447576725034118526046292574067040720093

# sp.var('p, q')
# eq1 = sp.Eq(p * q, N)
# eq2 = sp.Eq(2 * p + q, M)

# print(sp.solve([eq1, eq2], [p, q]))

p = 156360061061064414729350718107475156647696201916384475612165917151672039681953764020196675326794562949007314776569034065998332428376637134929798264399554687150921485448111123851340681028588745762599419292488809801223379887411755235919011704285719068065088499511780173937749645644749974003587069699717535256309
q = 142334186062265063219356604202944121242754649133715704144297972545346872221408855701425640596353771233387545377931080775413744238487922734779839556466413299896274963598187720052834744985690699039533532577445584533324042810567244036823175875348131212319476440307897156023046225832535991641744231454550103900877

l = lcm(p - 1, q - 1)

λ = lcm(p-1, q-1)
_, a, _ = ex_euclid(e, l)
d = a % l

print(e, d, N)

print(c, e, d)
p = pow(c, d, N)

h = hex(p)[2:]
print(h)

flag = ''
for i in range(0, len(h), 2):
    flag+= chr(int(h[i:i+2], 16))

print(flag)







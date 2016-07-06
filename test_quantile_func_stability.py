dist = 'Beta()'
dist_name = 'dist'

script_file_name = 'test_quantile_newton.jl'

int_name = 'int_var'
float32_name = 'float32_var'
float64_name = 'float64_var'
dual_name = 'dual_var'

int_init = int_name + ' = 1\n'
float32_init = float32_name + ' = 0.5f0\n'
float64_init = float64_name + ' = 0.5\n'
dualnum_init = dual_name + ' = ForwardDiff.Dual(0.5)\n'

var_types = ['int', 'float32', 'float64', 'dual']
vars = [int_name, float32_name, float64_name, dual_name]

def print_code_warntype_for_qnewton(f, var_type, dist, p, xs, tol):
    f.write('println("____________________________")\n')
    f.write('println("' + var_type + '")\n')
    f.write('println("____________________________")\n')
    f.write('@code_warntype Distributions.quantile_newton(' + dist + ', ' + p + ', ' + xs + ', ' + tol + ')\n')
    f.write('println()\n')

with open(script_file_name, 'w') as f:
    f.write('using Distributions\n')
    f.write('using ForwardDiff\n\n')

    f.write(dist_name + ' = ' + dist + '\n\n')

    f.write(int_init)
    f.write(float32_init)
    f.write(float64_init)
    f.write(dualnum_init)
    f.write('\n')

    for i in range(0,4):
        var_type = var_types[i]
        var = vars[i]
        print_code_warntype_for_qnewton(f, var_type, dist_name, float64_name, var, float64_name)



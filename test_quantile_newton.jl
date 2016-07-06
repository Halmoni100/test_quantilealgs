using Distributions
using ForwardDiff

dist = Beta()

int_var = 1
float32_var = 0.5f0
float64_var = 0.5
dual_var = ForwardDiff.Dual(0.5)

println("____________________________")
println("int")
println("____________________________")
@code_warntype Distributions.quantile_newton(dist, float64_var, int_var, float64_var)
println()
println("____________________________")
println("float32")
println("____________________________")
@code_warntype Distributions.quantile_newton(dist, float64_var, float32_var, float64_var)
println()
println("____________________________")
println("float64")
println("____________________________")
@code_warntype Distributions.quantile_newton(dist, float64_var, float64_var, float64_var)
println()
println("____________________________")
println("dual")
println("____________________________")
@code_warntype Distributions.quantile_newton(dist, float64_var, dual_var, float64_var)
println()

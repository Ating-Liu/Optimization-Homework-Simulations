import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
# from io import BytesIO # BytesIO 不再是必须的，除非您还想返回流

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# --- 约束条件 Ax = b ---
A1_CONSTRAINT, A2_CONSTRAINT, B_CONSTRAINT = 1.0, 0.5, 1.0
# 这对应直线: x1 + 0.5*x2 = 1  (或 x2 = 2 - 2*x1)

def objective_func_scipy(x1_val, p_norm, a1, a2, b_line):
    """目标函数，用于 scipy.optimize.minimize_scalar 来找到最优 x1."""
    if abs(a2) < 1e-9: 
        if abs(a1) < 1e-9: 
             return np.inf 
        x1_fixed = b_line / a1
        if abs(x1_val - x1_fixed) > 1e-7: 
            return np.inf
        return np.abs(x1_fixed)**p_norm
    
    x2_val = (b_line - a1 * x1_val) / a2
    return np.abs(x1_val)**p_norm + np.abs(x2_val)**p_norm

def plot_lp_level_set(ax, p_norm, radius_R, color='blue', line_style='-', label_override=None, zorder=1):
    """绘制 L_p 等值线 |x1|^p + |x2|^p = radius_R^p."""
    if radius_R < 1e-9: 
        ax.plot([0], [0], marker='o', color=color, label=f'$L_{{{p_norm:.1f}}}$ 等值线 (R≈0)', zorder=zorder)
        return

    x_coords_quad1 = np.linspace(0, radius_R, 200, endpoint=True)
    y_abs_p_part = radius_R**p_norm - x_coords_quad1**p_norm
    valid_indices = y_abs_p_part >= -1e-12 
    
    y_abs_p_part_safe = np.maximum(0, y_abs_p_part[valid_indices])
    x_coords_quad1_safe = x_coords_quad1[valid_indices]

    if len(x_coords_quad1_safe) == 0: 
        if radius_R > 0 : ax.plot([0],[0], marker='o', color=color, label=f'$L_{{{p_norm:.1f}}}$ 等值线 (R≈0)', zorder=zorder)
        return

    if p_norm == 0: 
        y_coords_quad1 = np.zeros_like(x_coords_quad1_safe) 
    else:
        y_coords_quad1 = y_abs_p_part_safe**(1/p_norm)

    label_text = label_override if label_override else f'$L_{{{p_norm:.1f}}}$ 等值线'

    ax.plot(x_coords_quad1_safe, y_coords_quad1, color=color, linestyle=line_style, zorder=zorder)
    ax.plot(x_coords_quad1_safe, -y_coords_quad1, color=color, linestyle=line_style, zorder=zorder)
    ax.plot(-x_coords_quad1_safe, y_coords_quad1, color=color, linestyle=line_style, zorder=zorder)
    ax.plot(-x_coords_quad1_safe, -y_coords_quad1, color=color, linestyle=line_style, label=label_text, zorder=zorder)
    
    if p_norm < 1.0 and p_norm != 0: 
        ax.plot([radius_R, -radius_R, 0, 0], [0, 0, radius_R, -radius_R], 
                marker='.', linestyle='None', markersize=4, color=color, alpha=0.6, zorder=zorder)


def generate_plots_for_p_range(p_values_list, main_title_suffix, constraint_params):
    """为给定的p值列表生成、显示并将图像保存到文件。""" # Docstring updated
    a1, a2, b_line = constraint_params
    num_p = len(p_values_list)
    fig, axes = plt.subplots(1, num_p, figsize=(6 * num_p, 6.5)) 
    if num_p == 1: axes = [axes] 

    plot_x_min = -1.5
    plot_x_max = 1.5 
    plot_y_min = -1.5
    plot_y_max = 2.5
    
    opt_search_bounds = (min(-1.0, plot_x_min), max(2.0, plot_x_max)) 

    for i, p_val in enumerate(p_values_list):
        ax = axes[i]
        x1_optimal, x2_optimal, R_optimal_norm = np.nan, np.nan, np.nan

        if abs(a2) > 1e-9: 
            result = minimize_scalar(objective_func_scipy, 
                                     args=(p_val, a1, a2, b_line), 
                                     bounds=opt_search_bounds, method='bounded')
            if result.success:
                x1_optimal = result.x
                x2_optimal = (b_line - a1 * x1_optimal) / a2
                optimal_sum_abs_p = result.fun 
                if optimal_sum_abs_p < 1e-12: 
                     R_optimal_norm = 0.0
                elif p_val == 0 : 
                     R_optimal_norm = optimal_sum_abs_p 
                else: 
                     R_optimal_norm = optimal_sum_abs_p**(1/p_val) 
            else:
                print(f"Warning: Optimization failed for p={p_val}")
        else: 
            if abs(a1) < 1e-9: 
                pass
            else:
                x1_optimal = b_line / a1
                x2_optimal = 0.0 
                optimal_sum_abs_p = np.abs(x1_optimal)**p_val
                if p_val == 0: 
                    R_optimal_norm = 1.0 if abs(x1_optimal) > 1e-9 else 0.0
                elif optimal_sum_abs_p < 1e-12:
                    R_optimal_norm = 0.0
                else:
                    R_optimal_norm = optimal_sum_abs_p**(1/p_val)

        x_line_vals = np.array([plot_x_min, plot_x_max])
        if abs(a2) > 1e-9:
            y_line_vals = (b_line - a1 * x_line_vals) / a2
            ax.plot(x_line_vals, y_line_vals, 'r--', alpha=0.7, label=f'约束: ${a1}x_1 + {a2}x_2 = {b_line}$', zorder=2)
        else: 
            ax.axvline(x=x1_optimal, color='r', linestyle='--', alpha=0.7, label=f'约束: ${a1}x_1 = {b_line}$', zorder=2)

        plot_lp_level_set(ax, p_val, 1.0, color='darkgrey', line_style=':', 
                          label_override=f'$L_{{{p_val:.1f}}}$ 单位等值线 ($R=1$)', zorder=1)
        
        if not np.isnan(R_optimal_norm):
            plot_lp_level_set(ax, p_val, R_optimal_norm, color='dodgerblue', line_style='-',
                              label_override=f'接触等值线 ($R={R_optimal_norm:.2f}$)', zorder=2)
        
        if not (np.isnan(x1_optimal) or np.isnan(x2_optimal)):
            ax.plot(x1_optimal, x2_optimal, 'go', markersize=10, alpha=0.8, label=f'最优点 $x^*$', zorder=3)
            x1_disp = 0.0 if abs(x1_optimal) < 1e-4 else x1_optimal
            x2_disp = 0.0 if abs(x2_optimal) < 1e-4 else x2_optimal
            title_text = (f'$p={p_val:.1f}$\n' 
                          f'$x^*=({x1_disp:.2f}, {x2_disp:.2f})$\n'
                          f'$||x^*||_{{{p_val:.1f}}} \\approx {R_optimal_norm:.2f}$')
        else:
            title_text = f'$p={p_val:.1f}$\n优化失败'
            
        ax.set_title(title_text, fontsize=10)
        ax.set_xlabel('$x_1$')
        ax.set_ylabel('$x_2$')
        ax.set_aspect('equal', adjustable='box')
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, fontsize='small', loc='upper right')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.axhline(0, color='black', lw=0.7, alpha=0.5)
        ax.axvline(0, color='black', lw=0.7, alpha=0.5)
        ax.set_xlim([plot_x_min, plot_x_max])
        ax.set_ylim([plot_y_min, plot_y_max])

    fig.suptitle(f'最小化 $L_p$ 范数，约束: ${a1}x_1+{a2}x_2={b_line}$ {main_title_suffix}', fontsize=14)
    plt.tight_layout(rect=[0, 0.02, 1, 0.95]) 
    
    # --- 修改部分：保存图像到文件 ---
    # 生成包含 p 值的动态文件名，确保文件名对于不同的 p 值组合是唯一的
    p_values_str = "_".join([f"p{pv:.1f}".replace('.', 'pt') for pv in p_values_list]) # e.g., p0pt5_p1pt5
    filename = f"lp_visualization_{p_values_str}.png"
    
    try:
        plt.savefig(filename, format="png", dpi=120) # 保存到文件
        print(f"图像已成功保存到: {filename}") # 告知用户成功
    except Exception as e:
        print(f"保存图像失败: {e}") # 告知用户失败原因
    # ---------------------------------
    
    plt.show() 
    
    plt.close(fig) 
    
    return filename # 返回保存的文件名

# --- 生成图像 ---
constraint = (A1_CONSTRAINT, A2_CONSTRAINT, B_CONSTRAINT)

p_values_custom = [0.5, 1.5] 
custom_title_suffix = "($p=0.5$ 与 $p=1.5$ 对比)"

# --- 调用函数生成、显示并保存图像 ---
saved_filename = generate_plots_for_p_range(p_values_custom, custom_title_suffix, constraint)

# print(f"脚本执行完毕，图像文件: {saved_filename}")
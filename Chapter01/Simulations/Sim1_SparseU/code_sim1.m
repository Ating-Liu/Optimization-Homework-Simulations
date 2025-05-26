% 设置参数
m = 128; % 矩阵A行数
n = 256; % 矩阵A列数（维度）
sparsity_ratio = 0.1; % u 中非零元素的比例

% 生成A、x、b
A = randn(m, n); % 高斯随机矩阵 A
u_original_sparse = sprandn(n, 1, sparsity_ratio);% 生成稀疏向量 u_original
u_original = full(u_original_sparse); % 转换为全向量方便后续计算和绘图
b = A * u_original;

% L2 范数最小化求解
% 解 x_l2 = A_pinv * b，其中 A_pinv 是 A 的伪逆
x_l2 = pinv(A) * b;

% L1 范数最小化求解
try
    cvx_begin quiet % quiet 模式减少输出
        variable x_l1(n) % 声明优化变量
        minimize(norm(x_l1, 1)) % 目标函数: 最小化 x 的 L1 范数
        subject to
            A * x_l1 == b; % 约束条件
    cvx_end % L1 最小化求解完成
    
    % 检查约束满足情况
    reconstruction_error_l1 = norm(A * x_l1 - b); % L1 解的重构误差
    fprintf('L1 solution reconstruction error ||Ax_l1 - b||_2: %e\n', reconstruction_error_l1);

catch ME
    x_l1 = nan(n,1); % 赋一个 NaN 值以便后续绘图部分能处理
end

reconstruction_error_l2 = norm(A * x_l2 - b); % 'L2 解的重构误差
fprintf('L2 solution reconstruction error ||Ax_l2 - b||_2: %e\n', reconstruction_error_l2);

% 可视化结果
figure('Name', 'L1 vs L2 Norm Minimization Comparison', 'Position', [100, 100, 800, 700]);

% 原始信号 u
subplot(3,1,1);
stem(1:n, u_original, 'MarkerFaceColor', 'b', 'MarkerSize', 4);
title(['原始稀疏信号 u (非零元素: ', num2str(nnz(u_original)), ')']);
xlim([1 n]);
grid on;

% L1 最小化解 x_l1
subplot(3,1,2);
if ~all(isnan(x_l1))
    stem(1:n, x_l1, 'MarkerFaceColor', 'r', 'MarkerSize', 4);
    title(['L1 最小化解 x_{L1} (非零元素阈值 > 1e-5: ', num2str(sum(abs(x_l1)>1e-5)), ')']);
    hold on;
    % 标记原始 u 中非零元素的位置，以便比较
    stem(find(u_original~=0), x_l1(u_original~=0), 'x', 'Color', [0.7 0 0], 'MarkerSize', 8, 'LineWidth', 1.5);
    legend('x_{L1}','Original non-zero pos.');
    hold off;
else
    text(0.5, 0.5, 'L1 解未计算成功', 'HorizontalAlignment', 'center');
    title('L1 最小化解 x_{L1}');
end
xlim([1 n]);
grid on;

% L2 最小化解 x_l2
subplot(3,1,3);
stem(1:n, x_l2, 'MarkerFaceColor', 'g', 'MarkerSize', 4);
title(['L2 最小化解 x_{L2} (非零元素阈值 > 1e-5: ', num2str(sum(abs(x_l2)>1e-5)), ')']);
hold on;
% 标记原始 u 中非零元素的位置
stem(find(u_original~=0), x_l2(u_original~=0), 'x', 'Color', [0 0.5 0], 'MarkerSize', 8, 'LineWidth', 1.5);
legend('x_{L2}','Original non-zero pos.');
hold off;
xlim([1 n]);
grid on;

sgtitle('原始信号、L1 解和 L2 解的比较');

% 输出解与原始信号的误差
if ~all(isnan(x_l1))
    solution_error_l1 = norm(x_l1 - u_original);
    fprintf('L1 solution error ||x_l1 - u_original||_2: %e\n', solution_error_l1);
end
solution_error_l2 = norm(x_l2 - u_original);
fprintf('L2 solution error ||x_l2 - u_original||_2: %e\n', solution_error_l2);

fprintf('Visualization complete.\n');
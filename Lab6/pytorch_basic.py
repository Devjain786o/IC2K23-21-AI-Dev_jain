
# Lab 6: PyTorch and Neural Network Implementation

import os
import matplotlib
matplotlib.use("Agg")

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Create required directories
os.makedirs("Lab6/outputs", exist_ok=True)
os.makedirs("models", exist_ok=True)

torch.manual_seed(42)

# ==========================================
# EXPERIMENT 1: TENSOR OPERATIONS
# ==========================================

print("EXPERIMENT 1: TENSOR OPERATIONS")

tensor_a = torch.tensor([1, 2, 3, 4])
tensor_b = torch.tensor([5, 6, 7, 8])

print("Tensor A:", tensor_a)
print("Tensor B:", tensor_b)
print("Addition:", torch.add(tensor_a, tensor_b))
print("Multiplication:", torch.mul(tensor_a, tensor_b))
print("Mean of A:", tensor_a.float().mean())

# ==========================================
# EXPERIMENT 2: AUTOMATIC DIFFERENTIATION
# ==========================================

print("\nEXPERIMENT 2: AUTOGRAD")

value = torch.tensor(2.0, requires_grad=True)
result = value ** 2

result.backward()

print("Input Value:", value.item())
print("Calculated Result:", result.item())
print("Gradient:", value.grad.item())

# ==========================================
# EXPERIMENT 3: LINEAR REGRESSION
# ==========================================

print("\nEXPERIMENT 3: LINEAR REGRESSION")

# Generate training data
features = torch.linspace(0, 10, 100).view(-1, 1)
labels = 3 * features + 2 + torch.randn(100, 1) * 0.5

# Initialize model
model_lr = nn.Linear(1, 1)

# Define loss and optimizer
loss_fn = nn.MSELoss()
optimizer_lr = torch.optim.SGD(model_lr.parameters(), lr=0.01)

training_losses = []

# Train the model
for step in range(500):
    predicted_values = model_lr(features)
    current_loss = loss_fn(predicted_values, labels)

    optimizer_lr.zero_grad()
    current_loss.backward()
    optimizer_lr.step()

    training_losses.append(current_loss.item())

print("Final Loss:", round(current_loss.item(), 4))
print("Learned Weight:", round(model_lr.weight.item(), 2))
print("Learned Bias:", round(model_lr.bias.item(), 2))

# Save trained model
torch.save(model_lr.state_dict(), "models/linear_regression.pth")

# Display regression graph
plt.figure(figsize=(8, 5))
plt.scatter(features.numpy(), labels.numpy(), label="Actual Data")
plt.plot(
    features.numpy(),
    model_lr(features).detach().numpy(),
    label="Predicted Line"
)

plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Linear Regression using PyTorch")
plt.legend()
plt.savefig("Lab6/outputs/linear_regression.png")
plt.show()

# ==========================================
# EXPERIMENT 4: XOR NEURAL NETWORK
# ==========================================

print("\nEXPERIMENT 4: NEURAL NETWORK")

# Define XOR input and output
xor_inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

xor_targets = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])

# Build neural network
model_nn = nn.Sequential(
    nn.Linear(2, 8),
    nn.Tanh(),
    nn.Linear(8, 1)
)

criterion_nn = nn.BCEWithLogitsLoss()
optimizer_nn = torch.optim.Adam(model_nn.parameters(), lr=0.05)

neural_losses = []

# Train the neural network
for step in range(2000):
    outputs = model_nn(xor_inputs)
    error = criterion_nn(outputs, xor_targets)

    optimizer_nn.zero_grad()
    error.backward()
    optimizer_nn.step()

    neural_losses.append(error.item())

# Predict XOR results
with torch.no_grad():
    probabilities = torch.sigmoid(model_nn(xor_inputs))

final_predictions = (probabilities >= 0.5).int()

print("Actual XOR Output:", xor_targets.int().flatten().tolist())
print("Predicted Output:", final_predictions.flatten().tolist())

# Save trained neural network
torch.save(model_nn.state_dict(), "models/xor_neural_network.pth")

# Plot training loss
plt.figure(figsize=(8, 5))
plt.plot(neural_losses)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Neural Network Training Loss")
plt.savefig("Lab6/outputs/neural_network_loss.png")
plt.show()

# ==========================================
# FINAL RESULT
# ==========================================

print("\nAll experiments completed successfully!")
print("Models and graphs saved successfully.")
print("LAB 6 COMPLETED.")

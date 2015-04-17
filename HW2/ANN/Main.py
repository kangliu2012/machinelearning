import copy;
from sigMod import sigMod;

learningRate = 0.1;

w1 = [[0.1,0.2,-0.1],
      [0.05,0.4,-0.2],
      [0.1,0.1,-0.1],
      [0.05,0.2,-0.2],
      [0.2,0.2,-0.2],
      [0.03,-0.2,-0.2],
      [-0.2,0.1,0.3],
      [0.5,0.2,-0.1]];
w2 = [[-0.1,0.1,-0.1,0.05,0.2,-0.2,0.05,0.2],
      [0.05,-0.22,-0.21,0.34,0.2,-0.2,0.05,0.2],
      [0.04,0.1,0.2,-0.5,-0.3,-0.2,0.05,0.2],
      ];

i1 = [[1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
      [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
      [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
      [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
      [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
      [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
      [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
      [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]];
o1 = copy.copy(i1);
tgt3 = copy.copy(o1);

i2 = [0.0,0.0,0.0];
o2 = copy.copy(i2);

i3 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0];
o3 = copy.copy(i3);

theta2 = [0,0,0];
theta3 = [0,0,0,0,0,0,0,0];

erro2 = copy.copy(o2);
erro3 = copy.copy(o3);

for kk in range(0, 10000):
    for ii in range(3, 4):
        #Propagate the inputs forward:
        #Middle Layer
        for j in range(0, 3):
            s = 0;
            for k in range(0, 8):
                s = s + w1[k][j] * o1[ii][k];
            i2[j] = s + theta2[j];
            o2[j] = sigMod(i2[j]);
        #Output Layer
        for j in range(0, 8):
            s = 0;
            for k in range(0, 3):
                s = s + w2[k][j] * o2[k];
            i3[j] = s + theta3[j];
            o3[j] = sigMod(i3[j]);
        #Backpropagate the errors:
        for i in range(0, 8):
            erro3[i] = o3[i] * (1 - o3[i]) * (tgt3[ii][i] - o3[i]);
        for i in range(0, 3):
            s = 0;
            for j in range(0, 8):
                s = s + erro3[j] * w2[i][j];
            erro2[i] = o2[i] * ( 1 - o2[i]) * s;
        for i in range(0, 3):
            for j in range(0, 8):
                w2[i][j] = w2[i][j] + learningRate * erro3[j] * o2[i];
        
        for i in range(0, 8):
            for j in range(0, 3):
                w1[i][j] = w1[i][j] + learningRate * erro2[j] * o1[ii][i]; 
    
        for i in range(0, 3):
            theta2[i] = learningRate * erro2[i];
        
        for i in range(0, 8):
            theta3[i] = learningRate * erro3[i];   

print o2;
print o3;

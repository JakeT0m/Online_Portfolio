%%Creating a Script to Investigate the Response of an LDR While Playing the
%%Dino game

%%Loading in the Values and Voltages
values = readtable('Values.txt');
voltages = readtable('Voltages.txt');

values = table2array(values);
voltages = table2array(voltages);

Fs = 20;    %Sampling Frequency (Hz)
%Creatimng the time series
samples = 0:(length(values)-1);
t = samples/Fs;

voltageLightMean = 1.3703;
valueLightMean = 10419.8020;

%%Plotting the Data
figure()
tiles = tiledlayout(2,1);

%First tile plot
nexttile
plot(t,values)
hold on
yline(valueLightMean)
title("LDR Values (Sampled at 20Hz)")
xlabel("Time")
ylabel("Value Amplitude")
legend("Value","Light Pixel Group Mean")
hold off

%Second tile Plot
nexttile
plot(t,voltages)
hold on
yline(voltageLightMean)
title("LDR Voltages (Sampled at 20Hz)")
xlabel("Time")
ylabel("Value Amplitude")
legend("Voltage","Light Pixel Group Mean")
hold off

title(tiles,"Investigating the Response of a LDR Whilst Playing the Dino Game")




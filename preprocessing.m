% Function For doing some preprocessing on the image in order to extract
% facial features more accurately


function result = preprocessing(a)


result = imresize(a, [119 102]);        % Resize image so that the resulting feature vector should be of same size 

result = rgb2gray(result);              % Convert image into greyscale

hgamma = vision.GammaCorrector(2.0, 'Correction', 'gamma'); % Setting the gamma correction threshold

result = step(hgamma, result);  % applying gamma correction
    
result=adapthisteq(result);     % For Histogram Equilization

result = extractHOGFeatures(result);    % Get HOG feature of the image

end




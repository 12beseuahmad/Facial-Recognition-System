% The matlab Script that will be called by python Server the input is the
% image and output is the label of the input image that is predicted
% through the model that was trained and saved on the disk

function label = predictlabel()

load('latestmodel.mat','svmstruct');                        % Load the trained model for prediction

x = imread('F:\r2015b\bin\communication\recieved.jpg');     % Read the input image that the server has saves on the disk
%x = imread('Umair1.jpg');
lbptest = preprocessing(x);                                 % extract features of this image that will be lates used for prediction

  l= vec2mat(lbptest,length(lbptest));                      % convert feature vector into matrix
  l1 = predict(svmstruct,l);                                % predict the label of the input image using its features
  
 label=l1;                                                  % Return label to python server

end

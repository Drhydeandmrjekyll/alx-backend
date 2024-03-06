// 7-job_processor.js

import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an Error object
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // Track progress to 50%
    job.progress(50, 100);
    
    // Log notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    
    // Finish job
    done();
  }
}

// Create Kue queue with concurrency 2
const queue = kue.createQueue({ concurrency: 2 });

// Process jobs in push_notification_code_2 queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

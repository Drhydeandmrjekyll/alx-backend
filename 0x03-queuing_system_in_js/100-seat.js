import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

// Promisify Redis functions
const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

// Initialize available seats to 50
reserveSeatAsync('available_seats', 50);

// Initialize reservationEnabled to true
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
    try {
        const numberOfAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
        res.json({ numberOfAvailableSeats });
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' });
        return;
    }

    try {
        const job = queue.create('reserve_seat').save();
        res.json({ status: 'Reservation in process' });
    } catch (error) {
        res.json({ status: 'Reservation failed' });
    }
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });
    queue.process('reserve_seat', async (job, done) => {
        try {
            const currentSeats = await getCurrentAvailableSeatsAsync('available_seats');
            const newSeats = parseInt(currentSeats, 10) - 1;

            if (newSeats === 0) {
                reservationEnabled = false;
            } else if (newSeats >= 0) {
                await reserveSeatAsync('available_seats', newSeats);
            } else {
                throw new Error('Not enough seats available');
            }

            console.log(`Seat reservation job ${job.id} completed`);
            done();
        } catch (error) {
            console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
            done(error);
        }
    });
});

app.listen(1245, () => {
    console.log('Server is running on port 1245');
});

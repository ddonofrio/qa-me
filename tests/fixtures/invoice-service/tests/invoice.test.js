import assert from 'node:assert/strict';
import { invoice } from '../invoice.js';
assert(invoice(10, 'customer@example.invalid'));
